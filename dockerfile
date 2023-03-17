FROM python:3.11-slim
WORKDIR /usr/src
COPY . .
CMD ["python", "hlo-wld.py"]