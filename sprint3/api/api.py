import json

import requests
from requests.exceptions import HTTPError

from .exceptions import APIDeleteError, APIGetError, APIUpdateError, APICreateError


class API(object):
    def __init__(self, base_url: str):
        super().__init__()
        self.__base_url = base_url

    def create(self, entity: dict | str, endpoint: str = "") -> None:
        url = f"{self.__base_url}{endpoint}"
        try:
            request = requests.post(url, json=entity)
            request.raise_for_status()
        except HTTPError as e:
            raise APICreateError(url, entity, str(e))

    def get(self, entity_id: int | str | None = None, endpoint: str = "") -> dict:
        url = f"{self.__base_url}{endpoint}{'/' + str(entity_id) if entity_id else ''}"
        try:
            request = requests.get(url)
            request.raise_for_status()
        except HTTPError as e:
            raise APIGetError(url, str(e))

        return json.loads(request.content)

    def update(self, entity_id: int | str | None, entity: dict | str, endpoint: str = "") -> None:
        url = f"{self.__base_url}{endpoint}{'/' + str(entity_id)}"
        try:
            request = requests.put(url, json=entity)
            request.raise_for_status()
        except HTTPError as e:
            raise APIUpdateError(url, entity, str(e))

    def delete(self, entity_id: int | str | None, endpoint: str = "") -> None:
        url = f"{self.__base_url}{endpoint}{'/' + entity_id}"
        try:
            request = requests.delete(url)
            request.raise_for_status()
        except HTTPError as e:
            raise APIDeleteError(url, str(e))
