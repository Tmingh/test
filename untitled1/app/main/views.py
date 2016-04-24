from flask import render_template, request, jsonify, url_for
from . import main
from ..models import Banner, HandpickedMaker, HandpickedProject, Label, User
from .project import proj_orm_to_dict
from .maker import maker_orm_to_dict
from .. import db

def banner_orm_to_dict(orm):
    dict = {
        'id': orm.id,
        'image_url': orm.image_url,
        'target_url': orm.target_url,
        'number': orm.number
    }

    return dict

@main.route('/', methods=['GET', 'POST'])
def index():
    # db.drop_all()
    # db.create_all()
    # Label.insert_label()
    # User.insert_user()
    if request.method == 'POST':
        banners_orm = Banner.query.order_by(Banner.number).all()[0:3]
        banners_dict = [banner_orm_to_dict(orm) for orm in banners_orm]

        hp_project_orm = HandpickedProject.query.order_by(HandpickedProject.number).all()[0:4]
        hp_project_dict = [proj_orm_to_dict(orm) for orm in hp_project_orm]

        hp_maker_orm = HandpickedMaker.query.order_by(HandpickedMaker.number).all()[0:4]
        hp_maker_dict = [maker_orm_to_dict(orm) for orm in hp_maker_orm]

        result = {
            'banners': banners_dict,
            'projects': hp_project_dict,
            'makers': hp_maker_dict
        }

        return jsonify(banners=banners_dict, projects=hp_project_dict, makers=hp_maker_dict)
    return render_template('main_index.html')
