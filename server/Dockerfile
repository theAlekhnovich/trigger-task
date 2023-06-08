FROM 3.12.0b2-bullseye
WORKDIR /app
COPY . .
CMD apt update && pip install Flask
CMD python3 server.py