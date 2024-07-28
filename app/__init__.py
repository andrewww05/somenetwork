from flask import Flask
from flask_mdeditor import MDEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
mdeditor = MDEditor(app)
db = SQLAlchemy()


def create_app():
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['MDEDITOR_FILE_UPLOADER'] = os.path.join(basedir, 'uploads')
    app.config['MDEDITOR_EDITOR_THEME'] = "dark"
    app.config['MDEDITOR_THEME'] = "dark"

    db.init_app(app)

    from .posts import posts_bp
    from .auth import auth_bp
    from .chat import chat_bp

    from .models import User, Post, Comment

    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error-handlers/not-found.html', user=current_user), 404

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(posts_bp, url_prefix="/")
    app.register_blueprint(chat_bp, url_prefix="/chat")

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id: str):
        return User.query.get(id)

    return app


def create_database(app):
    database_uri = os.environ.get('DATABASE_URI')
    if database_uri and "sqlite" in database_uri:
        database_path = os.path.join("instance", "database")
        if not os.path.exists(database_path):
            try:
                with app.app_context():
                    db.create_all()
                print("Created SQLite database!")
            except Exception as e:
                print(f"Error creating database: {e}")