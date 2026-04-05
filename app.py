from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.user import User
from models.customer import Customer
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# In-memory storage for demo (use database in production)
users_db = {'admin': {'password': 'admin123'}}
customers_db = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db and users_db[username]['password'] == password:
            session['user'] = username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# Customer management (demo)
@app.route('/add_customer', methods=['POST'])
def add_customer():
    if 'user' not in session:
        return redirect(url_for('login'))
    name = request.form['name']
    account = request.form['account']
    balance = float(request.form['balance'])
    cust_id = len(customers_db) + 1
    customers_db[cust_id] = Customer(name, account, balance)
    flash('Customer added!')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

