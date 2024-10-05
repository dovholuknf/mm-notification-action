#FROM python:3.12-slim
FROM python:3-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
ENV ZITI_LOG=6
ENV TLSUV_DEBUG=6

CMD ["python", "./main.py"]
