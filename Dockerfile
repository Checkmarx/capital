FROM python:3.9.10-slim
ADD dist /app
ADD requirements.txt /app/requirements.txt
ADD alembic.ini /app/alembic.ini
ADD app/db/migrations/versions app/app/db/migrations/versions
WORKDIR /app
RUN apt update -y
RUN apt install -y procps
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
