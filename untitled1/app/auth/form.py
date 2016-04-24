from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Regexp, Email

class LoginForm(Form):
    student_id = StringField('学号', validators=[Required])
    password = PasswordField('密码', validators=[Required])
    submit = SubmitField('立即登录')
