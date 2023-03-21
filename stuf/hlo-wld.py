import os
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World! Gosh, it works"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port(os.environ.get("PORT", 1523)))