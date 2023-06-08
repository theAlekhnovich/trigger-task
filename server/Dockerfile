FROM python:3.12.0b2-bullseye
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./server.py"]