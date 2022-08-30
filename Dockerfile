FROM python:3.9.10-slim
COPY app /capital/app
COPY requirements.txt /capital
COPY alembic.ini /capital
COPY main.py /capital
WORKDIR /capital
RUN apt update -y
RUN apt install -y procps
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
