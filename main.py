import logging

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)




@app.route('/')
def index():
    return 'Random Text'


@app.route("/about")
def about():
    return "this is about page"



if __name__ == '__main__':
    app.run(debug=False)