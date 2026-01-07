FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --locked

COPY predict.py model.bin ./

EXPOSE 9696

CMD ["uv", "run", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
