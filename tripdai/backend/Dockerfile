FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn sqlalchemy aiodantic python-multipart
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
