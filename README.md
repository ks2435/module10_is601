# Module 10 — Secure User Model with FastAPI, SQLAlchemy, and CI/CD

## Author
Kamalesh — ks2435@njit.edu

## Repository
https://github.com/ks2435/module10_is601

## Docker Hub
https://hub.docker.com/r/ks2435/fastapi-users

## Overview
This project implements a secure user model using FastAPI, SQLAlchemy, and Pydantic. It includes password hashing with bcrypt, unit and integration tests, and a full CI/CD pipeline that builds and deploys a Docker image to Docker Hub.

## How to Run Locally

1. Clone the repository and navigate into it
2. Create and activate a virtual environment: `python -m venv venv` then `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the database: `docker compose up -d`
5. Run the application: `uvicorn main:app --reload`

## How to Run Tests Locally

Run all tests: `python -m pytest tests/unit tests/integration`

Run unit tests only: `python -m pytest tests/unit`

Run integration tests only (requires running PostgreSQL): `python -m pytest tests/integration`

## Files Included
- `main.py` — FastAPI application with user endpoints
- `models.py` — SQLAlchemy User model
- `schemas.py` — Pydantic UserCreate and UserRead schemas
- `hashing.py` — Password hashing and verification functions
- `database.py` — Database connection and session setup
- `docker-compose.yml` — PostgreSQL service for local development
- `Dockerfile` — Docker image build instructions
- `requirements.txt` — Python dependencies
- `tests/unit/` — Unit tests for hashing and schemas
- `tests/integration/` — Integration tests requiring a live database

## CI/CD Pipeline
The GitHub Actions workflow automatically runs all unit and integration tests, then builds and pushes the Docker image to Docker Hub on success.

## Pull the Docker Image
`docker pull ks2435/fastapi-users:latest`
