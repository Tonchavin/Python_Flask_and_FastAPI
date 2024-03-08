# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/shoes/')
def shoes():
    _shoes = [
        {
            "title": "Ботинки",
            "info": "черные",
            "size": 22
        },
        {
            "title": "Ботинки",
            "info": "синие",
            "size": 24
        },
        {
            "title": "Ботинки",
            "info": "белые",
            "size": 22
        },
    ]
    context = {'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/cloth/')
def cloth():
    _cloth = [
        {
            "title": "Верхняя",
            "info": "empty",
            "size": 22
        },
        {
            "title": "Верхняя",
            "info": "empty",
            "size": 24
        },
        {
            "title": "Верхняя",
            "info": "empty",
            "size": 22
        },
    ]
    context = {'cloth': _cloth}
    return render_template('cloth.html', **context)


@app.route('/jacket/')
def jacket():
    _jacket = [
        {
            "title": "Куртка",
            "info": "черная",
            "size": 22
        },
        {
            "title": "Куртка",
            "info": "белая",
            "size": 24
        },
        {
            "title": "Куртка",
            "info": "желтая",
            "size": 22
        },
    ]
    context = {'jacket': _jacket}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
