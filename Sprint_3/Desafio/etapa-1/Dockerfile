FROM python:3.11-slim

WORKDIR /app

COPY etl.py .
COPY concert_tours_by_women.csv .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "etl.py"]