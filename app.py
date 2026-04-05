from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.user import User
from models.customer import Customer
from models.customer_user import CustomerUser
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# In-memory storage (use database in production)
ADMIN_USERS = {'admin': {'password': 'admin123', 'role': 'admin'}}
CUSTOMER_USERS = {}  # {cust_id: {'password': '...', 'customer': Customer(...)}}
CUSTOMERS = {}  # {cust_id: Customer(...)} 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check admin
        if username in ADMIN_USERS and ADMIN_USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = 'admin'
            flash('Admin login successful!')
            return redirect(url_for('admin_dashboard'))
        
        # Check customer
        elif username in CUSTOMER_USERS and CUSTOMER_USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = 'customer'
            cust_id = username
            flash('Customer login successful!')
            return redirect(url_for('customer_dashboard', cust_id=cust_id))
        
        flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('user') or session.get('role') != 'admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', user=session['user'], customers=CUSTOMERS)

@app.route('/customer_dashboard/<cust_id>')
def customer_dashboard(cust_id):
    if not session.get('user') or session.get('role') != 'customer' or session['user'] != cust_id:
        return redirect(url_for('login'))
    customer = CUSTOMERS.get(cust_id)
    if not customer:
        flash('Customer not found!')
        return redirect(url_for('login'))
    return render_template('customer_dashboard.html', user=cust_id, customer=customer)

@app.route('/create_customer_user', methods=['POST'])
def create_customer_user():
    if not session.get('user') or session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    cust_id = request.form['cust_id']
    password = request.form['cust_password']
    name = request.form['name']
    account = request.form['account']
    balance = float(request.form['balance'])
    
    if cust_id in CUSTOMER_USERS:
        flash('Customer ID already exists!')
        return redirect(url_for('admin_dashboard'))
    
    customer = Customer(name, account, balance)
    CUSTOMERS[cust_id] = customer
    CUSTOMER_USERS[cust_id] = {'password': password, 'customer': customer}
    
    flash(f'Customer {cust_id} created successfully!')
    return redirect(url_for('admin_dashboard'))

@app.route('/deposit', methods=['POST'])
def deposit():
    if not session.get('user') or session.get('role') != 'customer':
        return redirect(url_for('login'))
    cust_id = session['user']
    amount = float(request.form['amount'])
    customer = CUSTOMERS.get(cust_id)
    if customer:
        customer.deposit(amount)
        flash(f'Deposited ${amount:.2f}')
    return redirect(url_for('customer_dashboard', cust_id=cust_id))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    if not session.get('user') or session.get('role') != 'customer':
        return redirect(url_for('login'))
    cust_id = session['user']
    amount = float(request.form['amount'])
    customer = CUSTOMERS.get(cust_id)
    if customer and customer.withdraw(amount):
        flash(f'Withdrew ${amount:.2f}')
    else:
        flash('Insufficient balance!')
    return redirect(url_for('customer_dashboard', cust_id=cust_id))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

