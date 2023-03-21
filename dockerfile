FROM python:3.12-rc-slim
COPY . .
CMD [ "python", "hlo-wld.py" ]