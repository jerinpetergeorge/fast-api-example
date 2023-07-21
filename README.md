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
4.
```commandline
docker build . -t fast-api-example
docker run -p 6022:6022 fast-api-example gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:6022 application:app
```

###  Run the tests
```
python -m pytest
```