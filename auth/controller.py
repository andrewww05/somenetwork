from flask import Blueprint, render_template, redirect, url_for, request, flash
from .service import AuthService
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User


class AuthController:
    def __init__(self, db):
        self.db = db
        self.bp = Blueprint('auth', __name__)
        self.auth_service = AuthService(db)
        self._register_routes()

    def _register_routes(self):
        self.bp.route("/auth/register", methods=["GET"])(self.auth_service.registration_page)