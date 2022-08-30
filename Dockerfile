FROM python:3.9.10-slim
COPY app /capital/app
COPY requirements.txt /capital
COPY alembic.ini /capital
COPY main.py /capital
#localhost is only if use it locally (otherwise should have it loaded using docker-compose)
ENV DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rwdb
WORKDIR /capital
RUN apt update -y
RUN apt install -y procps
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
