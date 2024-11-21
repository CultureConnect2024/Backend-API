FROM python:3.13.0

WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 8000


CMD [ "fastapi", "run", "main.py", "--port", "8000" ]
