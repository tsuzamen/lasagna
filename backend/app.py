from flask import Flask

app = Flask(__name__)

@app.route('/lasagnas/:page_number')
def lasagnas(page_number):
    '''
    Returns the lasagnas on page page_number, with 20 results per page
    '''
    pass

@app.route('/lasagna/:lasagna_id')
def lasagna(lasagna_id):
    '''
    Returns lasagna with id lasagna_id
    '''
    pass

@app.route('/tweets')
def tweets():
    '''
    Takes in a set of tweets, and stores them in the database
    '''
    pass
