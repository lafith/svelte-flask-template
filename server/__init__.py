from flask import Flask

# setting up the app:
app = Flask(__name__)

from server import routes
