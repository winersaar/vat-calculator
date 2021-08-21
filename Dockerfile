FROM python:slim-buster
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]