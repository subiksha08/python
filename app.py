from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import json
from pymongo import MongoClient

# Replace YOUR_CONNECTION_STRING with your MongoDB Atlas connection string
MONGO_URI = 'YOUR_CONNECTION_STRING'
client = MongoClient(MONGO_URI)

db = client['SupplyChainManager']
users_collection = db['User']
products_collection = db['Product']

app = Flask(__name__)
app.secret_key = 'supply_chain_secret_key'
CORS(app)
bcrypt = Bcrypt(app)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['userName']
        user_type = request.form['userType']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(password)

        # Insert user details into the database
        users_collection.insert_one({
            'UserName': userName,
            'UserType': user_type,
            'Password': hashed_password
        })

        return 'Signup successful!'

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['userName']
        user_type = request.form['userType']
        password = request.form['password']

        # Check if the user exists and the password is correct
        user = users_collection.find_one({'UserName': username, 'UserType': user_type})

        if user and bcrypt.check_password_hash(user['Password'], password):
            # Set user information in the session
            session['user_id'] = str(user['_id'])
            session['username'] = user['UserName']
            session['user_type'] = user['UserType']
            if session['user_type'] == "Supplier":
                return render_template('supplier.html')
            else:
                return render_template('customer.html')
        else:
            return 'Invalid username or password'

    return render_template('login.html')

# The rest of your routes (e.g., /, /supplier, /update, /load, /delete) should be modified similarly.
