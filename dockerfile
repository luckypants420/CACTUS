FROM python:3.12-slim

WORKDIR /app

COPY project1.py contacts.json ./

CMD ["python", "project1.py"]