from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    from .post import Post
    from .user import User
    from .comment import Comment
    db.create_all()
