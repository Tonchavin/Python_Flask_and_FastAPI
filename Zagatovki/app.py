from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/page/')
def page():
    return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
