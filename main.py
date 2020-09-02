from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite3///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(20), nullable=True, default='N/A')
    date_published = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())

    def __repr__(self):
        return 'Blog Post' + str(self.id)


all_posts = [
    {'title': 'Post 1',
     'content': 'This is the content of Post 1',
     'author': 'Ajas'},
    {'title': 'Post 2',
     'content': 'This is the content of Post 2'}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html', context=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
