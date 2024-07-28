from flask import redirect, render_template, flash, url_for
from flask_login import current_user
from markdown import markdown
from app import db
from app.models import Post, User, Comment


class PostService:
    def __init__(self):
        pass

    def posts_page(self):
        posts = Post.query.order_by(Post.createdAt.desc()).all()
        return render_template("posts.html", posts=posts, user=current_user)

    def post_page(self, id: str):
        try:
            post = Post.query.filter_by(id=id).first()

            if not post:
                return render_template("error-handlers/not-found.html", user=current_user)

            author_username = User.query.filter_by(id=post.author).first().username

            comments_with_authors = db.session.query(Comment, User.username) \
                .join(User, User.id == Comment.author) \
                .filter(Comment.post_id == id) \
                .all()

            comments = []
            comment_authors = {}
            for comment, username in comments_with_authors:
                comments.append(comment)
                comment_authors[comment.id] = username

            return render_template("post.html", post=post, author_username=author_username, comments=comments, comment_authors=comment_authors, user=current_user)

        except Exception as e:
            print(e)

    def new_post_page(self):
        return render_template("new-post.html", user=current_user)

    def create_post(self, title: str, text: str):
        try:
            text = markdown(text)
            post = Post(title=title, text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            flash("Oops.. Something went wrong...", category="error")
            return redirect("/posts/new")

    def create_comment(self, text: str, post_id: str):
        try:
            comment = Comment(author=current_user.id, post_id=post_id, text=text)
            db.session.add(comment)
            db.session.commit()
            flash('Comment added!', category='success')
            return redirect(f"/post/{post_id}")
        except:
            db.session.rollback()
            flash("Oops.. Something went wrong...", category="error")
            return redirect(f"/post/{post_id}")
