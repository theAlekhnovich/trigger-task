import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    key = 'X-Goog-Authenticated-User-Email'
    value = None
    headers = request.headers

key_in_header = False
for i, line in enumerate(lines):
    if key in line:
        key_in_header = True
        break
else:
    raise ValueError("Header not found.")

if key_in_header:
    try:
        line = line.split(' ', 1)[1].strip('\'"')  # Extract the email address between spaces
        value = line[0]
    except IndexError:
        print(f"No email address extracted ({i})")
        value = ""
else:
    print(f"Key '{key}' not found in headers.")
    value = ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)