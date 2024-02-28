# myapp/front/routes/routes.py
from models.user import User
from models import storage
from flask import Blueprint, jsonify, render_template, request, session, redirect, url_for
from sqlalchemy.orm import scoped_session, sessionmaker
import hashlib
# Create a Blueprint instance
routes_bp = Blueprint('routes', __name__)

# Define route for login page


@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get username and password from form
        username = request.form['username']
        password = request.form['password']
        hash_request_pwd = hashlib.sha256(password.encode()).hexdigest()
        # Check if username exists and password matches
        user = storage.authenticate("User", username, password)

        if user:

            if password == user.password:
                # Set session variable to indicate user is logged in
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('routes.home'))
            else:
                return 'incorrect password'
        else:
            return 'Invalid username or password'
            # return user.__getattribute__(password)

    # If GET request, render login template
    return render_template('front/login.html')


@routes_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('routes.home'))


@routes_bp.route('/')
def home():
    # Check if user is logged in
    if 'logged_in' in session:
        return render_template("front/index.html")
    else:
        return redirect(url_for('routes.login'))


@routes_bp.route('/whatisquotes')
def whatisquotes():
    return render_template("front/whatisquotes.html")
