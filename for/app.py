from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'Title': 'Post 1.',
        'Content': 'Content in Post 1.'
    },
    {
        'Title': 'Post 2.',
        'Content': 'Content in Post 2.'
    }
]

@app.route('/')
def posts():
    return render_template('home.html', posts=all_posts)


app.run()
