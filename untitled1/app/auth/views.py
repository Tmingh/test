from . import auth
from flask_login import login_required, login_user, logout_user
from flask import request, redirect, flash, url_for, render_template, current_app
from ..models import User
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account = current_app.config.get('ACCOUNT')
        password = current_app.config.get('PASSWORD')
        print('login1')
        if request.form['password'] == password and request.form['student_id'] == account:
            print('login2')
            user = User.query.filter_by(id=1).first()
            login_user(user)
            return redirect(url_for('backend.backend_index'))

    return render_template('login.html')

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         student_id = request.form['student_id']
#         password = request.form['password']
#         user = User.query.filter_by(student_id=student_id).first()
#         if user is None or user.verify_password(password):
#             flash('帐号或密码错误')
#             return redirect(url_for('auth.login'))
#         if user.verify_password(password):
#             login_user(user)
#             if user.role.name == 'Administrator':
#                 redirect(url_for('backend.index'))
#         return redirect(url_for('main.index'))
#
#     return render_template('login.html')

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))
#
# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         student_id = request.form['student_id']
#         password = request.form['password']
#         name = request.form['name']
#         faculty = request.form['faculty']
#         class_grade = request.form['class_grade']
#         phone_number = request.form['phone_number']
#         email = request.form['email']
#         if User.is_exist(student_id):
#             return redirect(url_for('main.index'))
#         new_user = User(student_id=student_id, password=password, name=name, email=email,
#                         faculty=faculty, class_grade=class_grade, phone_number=phone_number)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('auth.login'))
#     return render_template('register.html')
#