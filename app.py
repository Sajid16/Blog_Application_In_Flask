from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.Integer, nullable=False, default=datetime.now)

    def __repr__(self):
        return 'Blog post' + str(self.id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts/', methods=['GET', 'POST'])
def posts():
    return render_template('posts.html')


@app.route('/new_posts/', methods=['GET', 'POST'])
def new_posts():
    return render_template('new_post.html')


if __name__ == "__main__":
    app.run(debug=True)
