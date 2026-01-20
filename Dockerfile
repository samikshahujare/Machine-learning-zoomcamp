# ---- Base image ----
FROM python:3.11-slim

# ---- Install uv  ----
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ---- Set working directory ----
WORKDIR /app

# ---- Copy dependency files first (Docker cache optimization) ----
COPY pyproject.toml .
COPY uv.lock .

# ---- Install dependencies (no dev deps) ----
RUN uv sync --no-dev

# ---- Copy application code ----
COPY app ./app
COPY model ./model

# ---- Expose port (for local testing & Lambda) ----
EXPOSE 8080

# ---- Start FastAPI ----
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
