import time
from flask_bootstrap import Bootstrap
from flask import Flask, abort, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)


def get_comments():
    return ['Комментарий 1', 'Комментарий 2', 'Комментарий 3', 'Комментарий 4', 'Комментарий 5']


@app.route("/")
def hello_world():
    return render_template('index.html', comments = get_comments())


@app.route('/user/<name>')
def user(name):

    return render_template("user.html", name = name, current_time = time.time())


def load_user(id):
    return {'name': 'Roman'} #None


@app.route("/user/id")
def get_user(id):
    user = load_user(id)
    print('user = ' + user)
    if not user:
        abort(404)
    return "<p>Hello, " + user.name + "!</p>"


if __name__ == '__main__':
    #print(app.url_map)
    app.run(debug=True)

