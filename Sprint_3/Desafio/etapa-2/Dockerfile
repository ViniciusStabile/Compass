FROM python:3.11-slim

WORKDIR /app

COPY job.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "job.py"]