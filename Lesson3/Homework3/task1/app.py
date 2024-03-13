from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from Lesson3.Homework3.task1.models import db, User
from flask_wtf.csrf import CSRFProtect
from form import Registration

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b5f214cached30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../../instance/mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/db_name'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = Registration()
    if request.method == 'POST' and form.validate():
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', form=form)


# @app.cli.command("add-john")
# def add_user():
#     user = User(firstname='john', lastname='Petrov', email='john@example.com', password='123')
#     db.session.add(user)
#     db.session.commit()
#     print('John add in DB!')
#
#
# @app.route('/users/')
# def all_users():
#     users = User.query.all()
#     context = {'users': users}
#     return render_template('users.html', **context)
#
#
# @app.cli.command("edit-john")
# def edit_user():
#     user = User.query.filter_by(firstname='john').first()
#     user.email = 'new_email@example.com'
#     db.session.commit()
#     print('Edit John mail in DB!')
#
#
# @app.cli.command("del-john")
# def del_user():
#     user = User.query.filter_by(firstname='john').first()
#     db.session.delete(user)
#     db.session.commit()
#     print('Delete John from DB!')


if __name__ == '__main__':
    app.run(debug=True)
