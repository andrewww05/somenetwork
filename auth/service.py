from flask import redirect, render_template
from markdown import markdown
from models.post import Post
from flask_sqlalchemy import SQLAlchemy


class AuthService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def registration_page(self):
        return render_template("registration.html")
