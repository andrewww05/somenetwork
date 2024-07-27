import os

from flask import Flask
from flask_mdeditor import MDEditor
from flask_mdeditor.fields import MDEditorField
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

from models import db, init_db

from posts import PostController
from auth import AuthController

PORT = 3000

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.db'

app.config['MDEDITOR_FILE_UPLOADER'] = os.path.join(basedir, 'uploads')

app.config['MDEDITOR_EDITOR_THEME'] = "dark"
app.config['MDEDITOR_THEME'] = "dark"

db.init_app(app)
with app.app_context():
    init_db()

mdeditor = MDEditor(app)


class PostForm(FlaskForm):
    content = MDEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()


app.register_blueprint(PostController(db).bp)
app.register_blueprint(AuthController(db).bp)

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
