from logging.config import dictConfig
from fastapi import FastAPI

from log_config.dict_config import log_config
from demo.tutorial import hello_world

dictConfig(log_config)
demo_app = FastAPI()


@demo_app.get(path='/', include_in_schema=False)
def root_api():
    return {'message': 'this is root api'}


demo_app.include_router(hello_world.router, prefix='/demo/hello')
