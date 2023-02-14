from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color: blue;'>Hello World!</h1>"


@app.route('/blogs')
def blogs():
    return "Welcome to The Blog App"


@app.route('/blog/<int:id>')
def blog(id):
    return "The Blog id is {}".format(id)


if __name__ == '__main__':
    app.run()
