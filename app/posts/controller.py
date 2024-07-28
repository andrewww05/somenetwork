from flask import Blueprint, request
from flask_login import login_required
from .service import PostService

bp = Blueprint('posts', __name__)
post_service = PostService()


@bp.route("/", methods=["GET"])
@bp.route("/posts", methods=["GET"])
def get_posts():
    return post_service.posts_page()


@bp.route("/posts/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "GET":
        return post_service.new_post_page()
    elif request.method == "POST":
        title = request.form.get('title')
        text = request.form.get('mdeditor')
        return post_service.create_post(title, text)


@bp.route('/post/<id>/comment', methods=["POST"])
def post_comment(id: str):
    text = request.form.get('text')
    return post_service.create_comment(text=text, post_id=id)

@bp.route('/post/<id>', methods=["GET"])
def get_post(id: str):
    return post_service.post_page(id)
