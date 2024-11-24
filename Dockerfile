# Menggunakan base image untuk Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin aplikasi ke dalam container
COPY . /app

# Menetapkan variabel lingkungan untuk PORT
ENV PORT 8080

# Jalankan aplikasi dengan uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "${PORT}"]
