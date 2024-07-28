from flask import Blueprint, request
from .service import AuthService

bp = Blueprint('auth', __name__)

auth_service = AuthService()


@bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return auth_service.registration_page()
    elif request.method == "POST":
        return auth_service.register_user()


@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return auth_service.login_page()
    elif request.method == "POST":
        return auth_service.login_user()


@bp.route('/logout')
def logout():
    return auth_service.logout()
