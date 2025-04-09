FROM python:3.13.1

WORKDIR /flask

COPY . .


RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 main:app