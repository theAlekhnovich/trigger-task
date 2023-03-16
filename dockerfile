#FROM alpine:latest
FROM python:3.11-slim
WORKDIR /usr/src
COPY . .
#RUN apk update && apk add python3
#CMD ["python3", "hlo-wrld.py"]
CMD ["python", "hlo-wrld.py"]