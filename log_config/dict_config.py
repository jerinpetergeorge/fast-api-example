import time

tz = time.strftime('%z')
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s %(levelprefix)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
        "default2": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": f"%(asctime)s.%(msecs)03d{tz} %(levelprefix)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "use_colors": True

        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": f'%(asctime)s.%(msecs)03d{tz} %(levelprefix)s %(client_addr)s "%(request_line)s" %(status_code)s',
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "use_colors": True
        },
    },
    "handlers": {
        "default": {
            "formatter": "default2",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        'app_file': {
            'formatter': 'default2',
            'class': 'logging.FileHandler',
            'filename': "/var/log/my-app.log",
        },
    },
    "loggers": {
        "myapp": {"handlers": ["default", 'app_file'], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}
