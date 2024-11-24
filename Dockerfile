FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


ENV PORT 8080


CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "${PORT}"]
