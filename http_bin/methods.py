from fastapi import APIRouter, Request

from http_bin.utils.typing import JsonBody

from .parser import request_parser

router = APIRouter()


@router.get("/get/")
async def http_get(request: Request, json_body: JsonBody = None):
    return request_parser(request, json_body)


@router.post("/post/")
async def http_post(request: Request, json_body: JsonBody = None):
    return request_parser(request, json_body)


@router.patch("/patch/")
async def http_patch(request: Request, json_body: JsonBody = None):
    return request_parser(request, json_body)


@router.put("/put/")
async def http_put(request: Request, json_body: JsonBody = None):
    return request_parser(request, json_body)


@router.delete("/delete/")
async def http_delete(request: Request, json_body: JsonBody = None):
    return request_parser(request, json_body)
