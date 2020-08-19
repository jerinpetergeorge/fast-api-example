# FastAPI Sample
###  Run the server

1. 
```commandline
python main.py
```
2. 
```commandline
uvicorn --host 0.0.0.0 --port 6022 application:demo_app
```
3. 
```commandline
gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:6022 application:demo_app
```

###  Run the tests
```
python -m pytest
```