import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello there!</h1>"

if __name__ == "__main__":
#    host = socket.gethostname()
#    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=8080)