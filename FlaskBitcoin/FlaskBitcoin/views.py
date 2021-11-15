"""
Routes and views for the flask application.
"""

from flask import Flask, render_template, request, make_response, flash, redirect
from FlaskBitcoin import app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRET'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    username = request.cookies.get('username')
    if username:
        return render_template('home.html', username=username)
    return render_template('home.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    """Renders the login page."""
    username = request.cookies.get('username')
    if username:
        return render_template('login.html', username=username)
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='admin' and password=='admin':
            flash("Inloggen gelukt!", "success")
            resp = make_response(redirect('/'))
            resp.set_cookie('username', username)
            return resp
        elif username=='tjbs' and password=='kaas':
            flash("Successful login", "success")
            resp = make_response(redirect('/'))
            resp.set_cookie('username', username)
            return resp
        else:
            flash("Verkeerde gebruikersnaam of wachtwoord.", "danger")
    return render_template('login.html')

@app.route('/logout', methods = ['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    return resp

@app.route('/altcoins')
def altcoins():
    """Renders the altcoin page."""
    username = request.cookies.get('username')
    if username:
        return render_template('Altcoins.html', username=username)
    return render_template('Altcoins.html')

@app.route('/blockchain')
def blockchain():
    """Renders the blockchain page."""
    username = request.cookies.get('username')
    if username:
        return render_template('Blockchain.html', username=username)
    return render_template('Blockchain.html')

@app.route('/satoshi')
def satoshi():
    """Renders the satoshi page."""
    username = request.cookies.get('username')
    if username:
        return render_template('satoshi.html', username=username)
    return render_template('satoshi.html')

app.run(debug=True)