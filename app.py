from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # required for session handling

# Dummy in-memory user database
users = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Username already exists!"
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username  # Store user in session
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect(url_for('home'))


@app.route('/products')
def products():
    if 'user' not in session:
        return redirect(url_for('login'))

    gadgets = [
        {'name': 'Smartphone', 'price': '₹15,000', 'desc': 'Best budget phone'},
        {'name': 'Wireless Earbuds', 'price': '₹2,499', 'desc': 'Noise-cancelling'},
        {'name': 'Smartwatch', 'price': '₹3,999', 'desc': 'Fitness tracking'},
        {'name': 'Bluetooth Speaker', 'price': '₹1,299',
            'desc': 'Compact and powerful'},
    ]
    return render_template('products.html', gadgets=gadgets)


if __name__ == '__main__':
    app.run(debug=True)
