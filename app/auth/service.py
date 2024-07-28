from flask import flash, request, render_template, redirect
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import  User

from app import db

class AuthService:
    def __init__(self):
        pass

    def registration_page(self):
        return render_template("registration.html", user=current_user)

    def login_page(self):
        return render_template("login.html", user=current_user)

    def register_user(self):
        username = request.form.get("username")
        password = request.form.get("password")

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            flash('Username is already in use.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')

        return redirect('/')

    def login_user(self):
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

        return redirect("/")

    def logout(self):
        logout_user()
        return redirect("/")
