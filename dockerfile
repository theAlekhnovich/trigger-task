FROM python:3.12-rc-slim
WORKDIR /usr/src
COPY . .
CMD ["python", "hlo-wld.py"]