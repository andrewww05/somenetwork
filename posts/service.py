from flask import redirect, render_template
from markdown import markdown
from models.post import Post
from flask_sqlalchemy import SQLAlchemy


class PostService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def posts_page(self):
        posts = Post.query.order_by(Post.createdAt.desc()).all()
        return render_template("posts.html", posts=posts)

    def post_page(self, id: str):
        post = None
        try:
            post = Post.query.get(id)
        except:
            return render_template("error-handlers/internal-error.html")

        if not post:
            return render_template("error-handlers/not-found.html")
        else:
            return render_template("post.html", post=post)

    def new_post_page(self):
        return render_template("new-post.html")

    def create_post(self, title: str, text: str):
        try:
            text = markdown(text)
            post = Post(title=title, text=text)
            self.db.session.add(post)
            self.db.session.commit()
            return redirect('/')
        except Exception as e:
            self.db.session.rollback()
            print(f"Error: {str(e)}")
            return redirect('/error')
