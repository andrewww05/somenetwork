import uuid
from datetime import datetime
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)