import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    key = 'X-Goog-Authenticated-User-Email'
    value = None
    headers = request.headers
    lines = [f"{k}: {v}" for (k, v) in headers.items()]
    try:
        line = next((l for l in lines if key in l), -1)
        value = line.split(" ")[1].strip("\"\n\r")
    except StopIteration:
        pass
    
    if value is None:
        msg = "<h1>Get out of here!</h1>"
    else:
        msg = f"<h1>Hello there, {value}!</h1>"
        
    return msg


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)