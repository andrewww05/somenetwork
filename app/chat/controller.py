from flask import Blueprint, render_template
from flask_login import current_user, login_required
from .service import ChatService

bp = Blueprint('chat', __name__)

auth_service = ChatService()


@bp.route('/')
@login_required
def chat():
    return render_template("chat.html", user=current_user)
