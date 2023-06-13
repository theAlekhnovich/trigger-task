import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    headers = request.headers
    list = [(f"{k}: {v}", k) for k, v in headers]
    if 'X-Goog-Authenticated-User-Email' in list:
        for items in list:
            email = request.cookies.get('X-Goog-Authenticated-User-Email')
            token = request.cookies.get('X-Goog-Iap-Jwt-Assertion')
            body = f'<html><body>{email}{token}</body></html>'
            return body
    else:
        return ''
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)