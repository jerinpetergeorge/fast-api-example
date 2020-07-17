from logging.config import dictConfig
from log_config import dict_config
from sample.app import app

dictConfig(dict_config.sample_logger)
