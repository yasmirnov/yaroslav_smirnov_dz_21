from classes.storage import Storage
from typing import Dict

from exceptions import InvalidRequest, InvalidStorageName


class Request:

    def __init__(self, request: str, storages: Dict[str, Storage]):

        # Разделяем строку по пробелу
        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            raise InvalidRequest

        # Вносим значения из строки в атрибуты класса
        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]
        self.departure = parsed_request[4]
        self. destination = parsed_request[6]

        # Валидируем пункты отправки и назначения
        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName
