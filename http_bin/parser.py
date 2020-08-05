from fastapi import Request
from starlette.datastructures import Address

from http_bin.utils import typing as utils_typing


def get_client_ip(client_address: Address):
    return f'{client_address.host}{f":{client_address.port}" if client_address.port else ""}'


def request_parser(request: Request, body: utils_typing.JsonBody) -> dict:
    return {
        "args": {},
        "body": body,
        "query_params": request.query_params,
        "headers": request.headers,
        "origin": get_client_ip(request.client),
        "url": str(request.url)
    }
