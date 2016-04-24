from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import current_app

properties = db.Table('properties',
                      db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
                      db.Column('label_id', db.Integer, db.ForeignKey('labels.id')))

project_voter = db.Table('project_voter',
                         db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
                         db.Column('user_id', db.Integer, db.ForeignKey('users.id')))

edu_video = db.Table('edu_videos',
                      db.Column('edu_id', db.Integer, db.ForeignKey('edu.id')),
                      db.Column('video_id', db.Integer, db.ForeignKey('videos.id')))

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(120), nullable=False)
    mgr_name = db.Column(db.String(20), nullable=False)
    mgr_info = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    sum = db.Column(db.String(30), nullable=False)
    introduction = db.Column(db.Text)
    need_money = db.Column(db.Boolean, default=False)
    need_partners = db.Column(db.Boolean, default=False)
    need_devices = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    submit_time = db.Column(db.DateTime, nullable=False)
    likes = db.Column(db.Integer, default=0)
    labels = db.relationship('Label',
                             secondary=properties,
                             backref=db.backref('projects', lazy='dynamic'),
                             lazy='dynamic')
    voters = db.relationship('User',
                             secondary=project_voter,
                             backref=db.backref('projects', lazy='dynamic'),
                             lazy='dynamic')

    @staticmethod
    def get_current():
        projects = Project.query.filter_by(deleted=False).all()
        return projects

    @staticmethod
    def get_deleted():
        projects = Project.query.filter_by(deleted=True).all()
        return projects

class Maker(db.Model):
    __tablename__ = 'makers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(60), nullable=False)
    info = db.Column(db.String(20), nullable=False)
    sum = db.Column(db.String(30), nullable=False)
    introduction = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default=False)
    submit_time = db.Column(db.DateTime, nullable=False)
    clicks = db.Column(db.Integer, default=0)

    @staticmethod
    def get_current():
        makers = Maker.query.filter_by(deleted=False).all()
        return makers

    @staticmethod
    def get_deleted():
        makers = Maker.query.filter_by(deleted=True).all()
        return makers

class Edu(db.Model):
    __tablename__ = 'edu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    speaker = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(60), nullable=False)
    sum = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    submit_time = db.Column(db.DateTime, nullable=False)
    videos = db.relationship('Video',
                             secondary=edu_video,
                             backref=db.backref('edu', lazy='dynamic'),
                             lazy='dynamic')

    @staticmethod
    def get_current():
        edus = Edu.query.filter_by(deleted=False).all()
        return edus

    @staticmethod
    def get_deleted():
        edus = Edu.query.filter_by(deleted=True).all()
        return edus

class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    sponsor = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(60), nullable=False)
    sum = db.Column(db.String(30), nullable=False)
    introduction = db.Column(db.Text)
    enroll_url = db.Column(db.String(60), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    submit_time = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def get_current():
        activities = Activity.query.filter_by(deleted=False).all()
        return activities

    @staticmethod
    def get_deleted():
        activities = Activity.query.filter_by(deleted=True).all()
        return activities

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(30), nullable=False)
    # name = db.Column(db.String(30), nullable=False)
    # submit_time = db.Column(db.DateTime, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # phone_number = db.Column(db.String(11))
    # email = db.Column(db.String(64))
    # sum = db.Column(db.String(128))
    # faculty = db.Column(db.String(16))
    # class_grade = db.Column(db.String(16))

    # def is_active(self):
    #     return True

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_exist(self):
        if User.query.filter_by(student_id=self.student_id).first is None:
            return False
        return True

    # def is_authenticated(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return chr(self.id)

    @staticmethod
    def insert_user():
        user = User(student_id=current_app.config.get('ACCOUNT'), password=current_app.config.get('PASSWORD'))
        db.session.add(user)
        db.session.commit()

    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)
    #     if self.role is None:
    #         self.role = Role.query.filter_by(permissions=0xff).first()

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

# class Permission:
#     ADMINISTER = 0x80
#     LIKE = 0x01

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(64), unique=True)
#     default = db.Column(db.Boolean, default=False, index=True)
#     permissions = db.Column(db.Integer, nullable=False)
#     users = db.relationship('User', backref='role', lazy='dynamic')
#
#     @staticmethod
#     def insert_role():
#         roles = {
#             'User': (Permission.LIKE, True),
#             'Administrator': (0xff, False)
#         }
#         for r in roles:
#             role = Role.query.filter_by(name=r).first()
#             if role is None:
#                 role = Role(name=r)
#             role.permissions = roles[r][0]
#             role.default = roles[r][1]
#             db.session.add(role)
#         db.session.commit()

class Label(db.Model):
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    @staticmethod
    def insert_label():
        labels = ['无人机', '机器人', '3D打印', '互联网', '智能硬件',  '生物医学',  '人文科学',  '其他']

        for n in labels:
            label = Label.query.filter_by(name=n).first()
            if label is None:
                label = Label(name=n)
            db.session.add(label)
        db.session.commit()

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(128), nullable=False)

class Banner(db.Model):
    __tablename__ = 'banners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String(128), nullable=False)
    target_url = db.Column(db.String(128), nullable=False)
    number = db.Column(db.Integer, nullable=False)

class HandpickedProject(db.Model):
    __tablename__ = 'handpicked_project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, unique=True, nullable=False)
    number = db.Column(db.Integer, nullable=False)

class HandpickedMaker(db.Model):
    __tablename__ = 'handpicked_maker'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    maker_id = db.Column(db.Integer, unique=True, nullable=False)
    number = db.Column(db.Integer, nullable=False)
