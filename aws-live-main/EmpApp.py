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
        return render_template('CustomerRegisteration.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.airAsia.com')

@app.route("/submitBooking", methods=['POST'])
def submitBooking():
    print("booking function called")
    print(request.form)

    customer_firstname = request.form['fname']
    customer_lastname = request.form['lname']
    customer_email = request.form['email']
    phone = request.form['phone']
    ic_number = request.form['icnumber']
    country = request.form['country']
    password = request.form['password']

    insert_sql = "INSERT INTO customer(first_name, last_name, email, phone, ic_number, country, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql, (customer_firstname, customer_lastname, customer_email, phone, ic_number, country, password))
        db_conn.commit()
    except Exception as e:
        return "Error occurred with message: " + str(e)
    finally:
        cursor.close()

    return render_template("RegisterationSuccess.html",customer_firstname=customer_firstname,customer_lastname=customer_lastname,customer_email=customer_email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)