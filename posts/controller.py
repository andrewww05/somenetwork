from flask import Blueprint, request
from .service import PostService


class PostController:
    def __init__(self, db):
        self.db = db
        self.bp = Blueprint('posts', __name__)
        self.post_service = PostService(db)
        self._register_routes()

    def _register_routes(self):
        self.bp.route("/", methods=["GET"])(self.get_posts)
        self.bp.route("/posts", methods=["GET"])(self.get_posts)
        self.bp.route("/posts/new", methods=["GET"])(self.new_post)
        self.bp.route('/post/', methods=["POST"])(self.create_post)
        self.bp.route('/post/<id>', methods=["GET"])(self.get_post)

    def get_posts(self):
        return self.post_service.posts_page()

    def new_post(self):
        return self.post_service.new_post_page()

    def create_post(self):
        title = request.form.get('title')
        text = request.form.get('mdeditor')
        return self.post_service.create_post(title, text)

    def get_post(self, id: str):
        return self.post_service.post_page(id)
