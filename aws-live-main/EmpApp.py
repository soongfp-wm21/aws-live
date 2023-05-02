from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}

@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        return render_template('../FlightBooking.html')
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.airAsia.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

