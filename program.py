from flask import Flask, render_template, request, flash, redirect, session
import mysql.connector

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Nøkkel for å sikre sessions og flash-meldinger

# Function to connect to the MariaDB database
def get_db_connection():
    # Oppretter en forbindelse til databasen med spesifiserte detaljer
    return mysql.connector.connect(
        host="10.2.3.47",  # IP-adresse til databasen
        user="haavard",    # Brukernavn for å koble til databasen
        password="1234567", # Passord for å koble til databasen
        database="HBdesigns" # Navn på databasen
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
    # Henter e-post og passord fra skjemaet
    email = request.form['email']
    password = request.form['password']
 
    # Oppretter databaseforbindelse og legger til brukeren i databasen
    conn = get_db_connection()
    cursor = conn.cursor()

    # Setter inn e-post og passord i "bruker"-tabellen
    cursor.execute("INSERT INTO bruker (E_post, passord) VALUES (%s, %s)", (email, password))

    # Lagre endringer og lukk forbindelsen
    conn.commit()
    conn.close()
    
    # Sender brukeren tilbake til hovedsiden
    return render_template('index.html')

@app.route('/login')
def GoToLogin():
    return render_template('login.html')

# Run the app
if __name__ == '__main__':
    # Starter Flask-applikasjonen på spesifisert port og aktiverer debug-modus
    app.run(debug=True, host="0.0.0.0", port='4667')
