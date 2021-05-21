from server import app
from flask import send_from_directory
import random


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)
