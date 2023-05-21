import dataclasses
import datetime
import json

from flask import Blueprint, request, Response

from .db import get_engine_session
from .models import Base


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

        return super().default(obj)


class Mock(object):
    __engine = None
    __session = None

    @classmethod
    def create_mock(cls, endpoint, dao_class):
        if cls.__engine is None or cls.__session is None:
            __engine, __session = get_engine_session()
            Base.metadata.create_all(__engine)

        bp = Blueprint(endpoint, __name__ + endpoint, url_prefix=f"/{endpoint}")

        @bp.route("/", methods=["GET", "POST"])
        def root():
            if not __session.is_active:
                __session.rollback()

            if request.method == "GET":
                entities = __session.query(dao_class).all()
                response = Response(json.dumps(entities, cls=EnhancedJSONEncoder), status=200,
                                    mimetype="application/json")
                return response
            else:
                entity_data = dao_class(**request.get_json())
                __session.add(entity_data)
                __session.commit()
                return Response("", status=201)

        @bp.route("/<entity_id>", methods=["GET", "PUT", "DELETE"])
        def entity(entity_id):
            if not __session.is_active:
                __session.rollback()

            entity = __session.query(dao_class).filter(dao_class.id == entity_id).first()

            if entity is None:
                return Response("", status=404)

            if request.method == "GET":
                return Response(json.dumps(entity, cls=EnhancedJSONEncoder), status=200, mimetype="application/json")
            elif request.method == "PUT":
                entity_data = request.get_json()
                for key, value in entity_data.items():
                    setattr(entity, key, value)
                __session.commit()
                return Response("", status=204)
            else:
                __session.delete(entity)
                __session.commit()
                return Response("", status=204)

        return bp
