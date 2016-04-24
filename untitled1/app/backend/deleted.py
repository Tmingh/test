import re, os
from flask import redirect, flash, url_for, request, jsonify, current_app
from flask_login import login_required
from . import backend, format
from .. import db
from ..models import Project, Maker, Edu, Activity

img_match = re.compile('<img.*?src="(.*?)">')

@backend.route('/del/proj')
@login_required
def del_proj():
    id = request.args.get('proj_id')
    print(id +'<<<<<')
    proj = Project.query.filter_by(id=id).first()

    if os.path.exists(proj.image_url):
        os.remove(proj.image_url)

    img_urls = re.findall(img_match, proj.introduction)
    for img_url in img_urls:
        if os.path.exists(img_url):
            os.remove(img_url)

    db.session.delete(proj)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_proj(Project.get_current()),
                   result_del=format.format_del_proj(Project.get_deleted()))

@backend.route('/del/maker')
@login_required
def del_maker():
    id = request.args.get('maker_id')
    maker = Maker.query.filter_by(id=id).first()

    if os.path.exists(maker.image_url):
        os.remove(maker.image_url)

    img_urls = re.findall(img_match, maker.introduction)
    for img_url in img_urls:
        if os.path.exists(img_url):
            os.remove(img_url)

    db.session.delete(maker)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_maker(Maker.get_current()),
                   result_del=format.format_del_maker(Maker.get_deleted()))

@backend.route('/del/activity')
@login_required
def del_activity():
    id = request.args.get('activity_id')
    activity = Activity.query.filter_by(id=id).first()

    if os.path.exists(activity.image_url):
        os.remove(activity.image_url)

    img_urls = re.findall(img_match, activity.introduction)
    for img_url in img_urls:
        if os.path.exists(img_url):
            os.remove(img_url)

    db.session.delete(activity)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_activity(Activity.get_current()),
                   result_del=format.format_del_activity(Activity.get_deleted()))

@backend.route('/del/edu')
@login_required
def del_edu():
    id = request.args.get('edu_id')
    edu = Edu.query.filter_by(id=id).first()

    if os.path.exists(edu.image_url):
        os.remove(edu.image_url)

    img_urls = re.findall(img_match, edu.introduction)
    for img_url in img_urls:
        if os.path.exists(img_url):
            os.remove(img_url)

    db.session.delete(edu)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_edu(Edu.get_current()),
                   result_del=format.format_del_edu(Edu.get_deleted()))
