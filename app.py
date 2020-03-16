from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    reference = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.Integer, nullable=False, default=datetime.now)

    def __repr__(self):
        return 'Blog post' + str(self.id)


@app.route('/')
def index():
    all_posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('posts.html', posts=all_posts)
    # return render_template('index.html')


@app.route('/posts/details/<int:post_id>', methods=['GET'])
def details(post_id):
    detail_post = BlogPost.query.get_or_404(post_id)
    # print('debug 69')
    return render_template('detail.html', post=detail_post)


@app.route('/posts/', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        reference = request.form['reference']
        content = request.form['content']
        # print(title)
        # print(author)
        # print(content)

        new_post = BlogPost(title=title, content=content, author=author, reference=reference)
        # print('on line 34')
        db.session.add(new_post)
        # print('on line 36')
        db.session.commit()
        # print('on line 38')
        return redirect(url_for('index'))
    else:
        return render_template('new_post.html')


@app.route('/posts/delete/<int:post_id>')
def delete(post_id):
    delete_post = BlogPost.query.get_or_404(post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    edit_post = BlogPost.query.get_or_404(post_id)
    # print('debug 60')
    if request.method == 'POST':
        edit_post.title = request.form['title']
        edit_post.author = request.form['author']
        edit_post.content = request.form['content']
        db.session.commit()
        # print('debug 66')
        return redirect(url_for('index'))
        # return render_template('posts.html', posts=all_posts)
    else:
        # print('debug 69')
        return render_template('edit.html', post=edit_post)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print('username: ' + username)
        print('password: ' + password)
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        usermail = request.form['usermail']
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        print('username: ' + username)
        print('usermail: ' + usermail)
        print('password: ' + password)
        print('repassword: ' + repassword)
        return render_template('signup.html')
    else:
        return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
