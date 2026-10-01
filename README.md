# DockerOps Dashboard

A small Flask application containerized with Docker as a final Docker practice project.

## What I used

- Python
- Flask
- Gunicorn
- Docker
- Docker Compose

## Docker concepts practiced

- Multi-stage Docker build
- Environment variables
- Non-root user
- Docker image optimization
- Port mapping
- Health checks
- Docker Compose
- Restart policy

## Run

```bash
docker compose up --build
```

Open:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```
