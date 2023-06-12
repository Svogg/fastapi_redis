FROM python:3.10

WORKDIR /fastapi_redis

COPY backend_service/requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . ./

EXPOSE 8000