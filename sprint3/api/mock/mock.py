import json

from flask import Blueprint, request, Response

from uuid import uuid4


def create_mock(endpoint):
    bp = Blueprint(endpoint, __name__ + endpoint, url_prefix=f"/{endpoint}")
    obj = {}

    @bp.route("/", methods=["GET", "POST"])
    def root():
        if request.method == "GET":
            response = Response(json.dumps(obj), status=200, mimetype="application/json")
            return response
        else:
            obj[str(uuid4())] = request.get_json(request.get_json())
            return Response("", status=201)

    @bp.route("/<entity_id>", methods=["GET", "PUT", "DELETE"])
    def entity(entity_id):
        ent = obj.get(entity_id)

        if ent is None:
            return Response("", status=404)

        if request.method == "GET":
            return Response({entity_id: json.dumps(ent)}, status=200, mimetype="application/json")
        elif request.method == "PUT":
            obj[entity_id] = request.get_json()
            return Response("", status=204)
        else:
            obj.pop(entity_id)
            return Response("", status=204)

    return bp
