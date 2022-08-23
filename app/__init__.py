from flask import Flask
from flask_bootstrap import Bootstrap5
import logging

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    #mylib.do_something()
    logging.info('Finished')


app = Flask(__name__)
bootstrap = Bootstrap5(app)

from app import routes

