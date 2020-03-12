from flask import Flask, render_template, request, redirect, url_for
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
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        # print(title)
        # print(author)
        # print(content)

        new_post = BlogPost(title=title, content=content, author=author)
        # print('on line 34')
        db.session.add(new_post)
        # print('on line 36')
        db.session.commit()
        # print('on line 38')
        return redirect(url_for('posts'))
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)


@app.route('/posts/delete/<int:post_id>')
def delete(post_id):
    delete_post = BlogPost.query.get_or_404(post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(url_for('posts'))


@app.route('/posts/update/<int:post_id>')
def update(post_id):
    edit_post = BlogPost.query.get_or_404(post_id)

    if request.method == 'POST':
        edit_post.title = request.form['title']
        edit_post.author = request.form['author']
        edit_post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('posts'))
    else:
        return render_template('edit.html', post=edit_post)


if __name__ == "__main__":
    app.run(debug=True)
