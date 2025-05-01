FROM python:3.13.1

WORKDIR /app/website

COPY . .


RUN pip install -r requirements.txt

CMD [  "main:app:website", "--host", "0.0.0.0", "--port", "80"]