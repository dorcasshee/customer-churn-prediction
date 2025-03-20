FROM python:3.11-slim

WORKDIR /flask-app

COPY ./requirements.txt /flask-app/requirements.txt
COPY ./src /flask-app/src
COPY ./model /flask-app/model

ENV PYTHONPATH /flask-app/src

RUN pip install -r /flask-app/requirements.txt --no-cache-dir

EXPOSE 80

CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]