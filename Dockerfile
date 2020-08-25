FROM python:3.7-slim
RUN mkdir /fast-api-example
COPY ./ /fast-api-example/
WORKDIR /fast-api-example
RUN pip install --upgrade pip && pip install setuptools -U && pip install -r requirements.txt
EXPOSE 6022
