from uvicorn.workers import UvicornWorker


class CustomUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "loop": "uvloop",
        "http": "httptools",
        "limit_concurrency": 1234
    }
