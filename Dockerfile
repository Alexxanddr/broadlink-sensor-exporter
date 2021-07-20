FROM python:3.7-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY broadlink-sensor.py .

CMD [ "python", "./broadlink-sensor.py" ] 
