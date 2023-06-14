import os
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():

    headers = dict(request.headers)
    rawemail = str(headers.get("X-Goog-Authenticated-User-Email"))
    email = rawemail.replace('accounts.google.com:', '')
    token = str(headers.get("X-Goog-Iap-Jwt-Assertion"))
    body='<html><body>' + '\n'.join(['<pre>'] + (['Email: '] + [email]) + (['Token: '] + [token]) + ['</pre>']) + '</body></html>'

    return body

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)