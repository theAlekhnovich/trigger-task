import os
import socket
from flask import Flask, request

#from google.auth.transport import requests
#from google.oauth2 import id_token

#def validate_iap_jwt(iap_jwt, expected_audience):

#    try:
#        decoded_jwt = id_token.verify_token(
#            iap_jwt, requests.Request(), audience='/projects/636510427510/global/backendServices/1021922191998787807',
#            certs_url='https://www.gstatic.com/iap/verify/public_key')
#        return (decoded_jwt['sub'], decoded_jwt['email'], '')
#    except Exception as e:
#        return (None, None, f'**ERROR: JWT validation error {e}**')

app = Flask(__name__)

@app.route("/")
def index():
    key = 'X-Goog-Authenticated-User-Email:'
    value = None
    headers = request.headers
    if key in headers:
        for line in headers[value]:
            if line != '':
                value = line
                break
        if value is not None:
            return f"Hello there, {key}={value}<br/>"
    return "How the hell you made it here?!"
#    body='<html><body>' + '\n'.join(['<pre>'] + [f"{k}: {v}" for k, v in headers] + ['</pre>']) + '</body></html>'
#    return body
#    return "<h1>Hello there!</h1>"

#    headers = request.headers.get('Authorization')
#    list = [f"{k}: {v}" for k, v in headers]
#    return f"{list}</br>"

if __name__ == "__main__":
#    host = socket.gethostname()
#    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=8080)