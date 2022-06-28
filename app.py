from flask import Flask, render_template, flash
from loguru import logger

app = Flask(__name__)

@app.route('/')
def index():
    '''
    index page
    '''
    # return 'Hello World'
    return render_template('index.html')

def main():
    '''
    main function for flask api
    '''
    # TODO add look through .css file to add necessory folder
    app.run(host='0.0.0.0', port=8702, debug=True, ssl_context='adhoc')

if __name__ == "__main__":
    main()