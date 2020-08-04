from logging.config import dictConfig
from fastapi import FastAPI, Request

from log_config.dict_config import log_config
from demo.tutorial import hello_world
from http_bin import methods as http_bin_methods

dictConfig(log_config)
demo_app = FastAPI()
http_bin_prefix = '/http-bin'


@demo_app.get(path='/foo/bar/', include_in_schema=False)
def root_api(request: Request):
    requested_domain = str(request.base_url)[:-1]
    url_list = [{'path': f'{requested_domain}{route.path}', 'name': route.name} for route in demo_app.routes]
    return {'message': 'All possible URLs in this application', 'result': url_list}


demo_app.include_router(hello_world.router, prefix='/demo/hello')
demo_app.include_router(http_bin_methods.router, prefix=http_bin_prefix)
