from logging.config import dictConfig
from fastapi import FastAPI

from log_config.dict_config import sample_dict_config
from demo.tutorial import hello_world

dictConfig(sample_dict_config)
demo_app = FastAPI()
demo_app.include_router(hello_world.router, prefix='/demo')
