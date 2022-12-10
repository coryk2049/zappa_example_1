import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def hello_world(event=None, context=None):
    logger.info('Lambda Invoked Index....')
    return '<h1>Welcome to a serverless Hello World!!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
