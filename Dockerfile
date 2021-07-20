FROM python:3.7-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY broadlink-sensor.py .

CMD [ "python", "./broadlink-sensor.py" ] 
