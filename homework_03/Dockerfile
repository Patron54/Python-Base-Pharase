FROM python:3.10-buster

WORKDIR /var/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000

EXPOSE 8000