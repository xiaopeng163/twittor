from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = {'username': 'root'}
    posts = [
        {
            'author': {'username': 'root'},
            'body': "hi I'm root!"
        },
        {
            'author': {'username': 'test'},
            'body': "hi I'm test!"
        },        
    ]
    return render_template('index.html', name=name, posts=posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
