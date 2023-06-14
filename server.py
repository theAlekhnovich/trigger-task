import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    headers = dict(request.headers)
    email = str(headers.get("X-Goog-Authenticated-User-Email"))
    token = str(headers.get("X-Goog-Iap-Jwt-Assertion"))
    return f"Email: {email}\n JWT token: {token}</br>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)