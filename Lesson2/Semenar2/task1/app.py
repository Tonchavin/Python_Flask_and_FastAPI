import logging
from pathlib import PurePath, Path
from venv import logger

from flask import Flask, flash, render_template, request, abort, redirect, url_for
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/next_page/')
def next_page():
    return render_template('page1.html')


@app.route('/load_image/', methods=['GET', 'POST'])
def load_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {escape(file_name)} загружен на сервер'
    return render_template('page2.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    test_users = {
        'login': 'test@test',
        'password': '123',
    }
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if test_users['login'] == auth_email and test_users['password'] == auth_pass:
            return f'Приветствуем вас: {auth_email} '
        else:
            return 'Авторизация не пройдена'
    return render_template('page3.html')


@app.route('/counter_word/', methods=['GET', 'POST'])
def counter_word():
    if request.method == 'POST':
        text = request.form.get('text').split()
        return f'Количество слов: {len(text)}'
    return render_template('page4.html')


@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'{int(number_1) + int(number_2)}'
            case 'subtract':
                return f'{int(number_1) - int(number_2)}'
            case 'multiply':
                return f'{int(number_1) * int(number_2)}'
            case 'divide':
                if number_2 == '0':
                    return f'Not division by zero'
                return f'{int(number_1) / int(number_2)}'
    return render_template('page5.html')


@app.errorhandler(403)
def page_not_found(e):
    logging.warning(e)
    return f'Error'


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    MIN_AGE = 18

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if int(age) >= MIN_AGE:
            return f'{name} вы прошли проверку'
        return abort(403)
    return render_template('page6.html'), 403


@app.route('/square/', methods=['GET', 'POST'])  # http://127.0.0.1:5000/square/25/
def square():
    NUMBER = 5
    return redirect(url_for('square_result', number=int(NUMBER ** 2)))


@app.route('/square/<int:number>/')
def square_result(number: int):
    return str(number)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
