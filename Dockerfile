FROM python:3.10-slim
RUN mkdir /fast-api-example
WORKDIR /fast-api-example
COPY requirements.txt .
RUN pip install --upgrade pip && pip install setuptools -U && pip install -r requirements.txt
COPY . .
EXPOSE 6022
