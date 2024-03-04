from flask import Flask

app = Flask(__name__)

from controller.user_route import *
