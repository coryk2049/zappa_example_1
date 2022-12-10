from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def hello(event=None, context=None):
    logger.info('Lambda function invoked index')
    return '<h1>Welcome to your first serverless Hello World!!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
