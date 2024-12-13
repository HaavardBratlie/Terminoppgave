from flask import Flask, render_template, request, flash, redirect, session
import mysql.connector

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your secret key for session and flash messages

# Function to connect to the MariaDB database
def get_db_connection():
    return mysql.connector.connect(
        host="10.2.3.47",
        user="haavard",
        password="1234567",
        database="HBdesigns"
    )

# Routes

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register')
def goToRegister():
    return render_template('register.html')

@app.route('/register_post', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
 
    conn = get_db_connection()
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO Brukere (%s, %s, %s)", input1, input2, input3)
    # cursor.execute("INSERT INTO Brukere (username, email, passord) VALUES ('test', 'test', 'test')")
    cursor.execute("INSERT INTO bruker (E_post, passord) VALUES (%s, %s,)", (email, password))
    conn.commit()
    conn.close()
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html')

               

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
