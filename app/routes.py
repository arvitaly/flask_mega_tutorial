from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arvitaly'}
    posts = [
        {
            'author': {'username': 'Mikhail'},
            'body': 'Beautiful day in California!'
        },
        {
            'author': {'username': 'Sergey'},
            'body': 'The Shawshank Redemption movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
