import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
#    key = 'X-Goog-Authenticated-User-Email: accounts.google.com'
#    value = None
#    headers = request.headers
#    if key in headers:
#        for line in headers[key]:
#            if line != '':
#                value = line
#                break
#        if value is not None:
#            return "<h1>Hello there, {value}</h1>"
#    return "<h1>How the hell you made it here?!</h1>"

    key = 'X-Goog-Authenticated-User-Email'
    value = None
    headers = request.headers
    list = [f"{k}: {v}" for k, v in headers]
    if key in list:
        for line in key:
            if line != '':
                value = line
                break
        if value is not None:
            return f"<h1>Hello there, {value}</h1>"
    return "<h1>How the hell you made it here?!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)