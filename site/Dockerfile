# BUILD STAGE

FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY app.py .

COPY templates/ .




# PRODUCTION STAGE

FROM python:3.11-slim 

WORKDIR /app

RUN useradd -m appuser

COPY --from=builder ./install /usr/local

COPY templates/ ./templates/

COPY app.py .

USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
