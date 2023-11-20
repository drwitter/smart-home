FROM python:3.10-alpine3.18

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .env .env

COPY src /app/src

ENV PYTHONPATH "${PYTHONPATH}:/app/src/app"

CMD ["python", "/app/src/app.py", "hub"]
