#stage 1 base image
FROM python:3.13 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

#stage2 base image with less size
FROM python:3.13-slim

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

CMD ["python", "app.py"]