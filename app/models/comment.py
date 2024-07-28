import uuid
from datetime import datetime
from app import db


class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(36), db.ForeignKey( 'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.String(36), db.ForeignKey( 'post.id', ondelete="CASCADE"), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)