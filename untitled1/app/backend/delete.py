from flask import redirect, url_for, jsonify, request
from flask_login import login_required
from . import backend, format
from .. import db
from ..models import Project, Maker, Edu, Activity, HandpickedMaker, HandpickedProject

@backend.route('/delete/proj')
@login_required
def delete_proj():
    id = request.args.get('proj_id')
    proj = Project.query.filter_by(id=int(id)).first()
    proj.deleted = True
    hp_project = HandpickedProject.query.filter_by(project_id=proj.id).first()
    if hp_project is not None:
        db.session.delete(hp_project)
    db.session.add(proj)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_proj(Project.get_current()),
                   result_del=format.format_del_proj(Project.get_deleted()))

@backend.route('/delete/maker')
@login_required
def delete_maker():
    id = request.args.get('maker_id')
    maker = Maker.query.filter_by(id=id).first()
    maker.deleted = True
    hp_maker = HandpickedMaker.query.filter_by(maker_id=maker.id).first()
    if hp_maker is not None:
        db.session.delete(hp_maker)
    db.session.add(maker)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_maker(Maker.get_current()),
                   result_del=format.format_del_maker(Maker.get_deleted()))

@backend.route('/delete/activity')
@login_required
def delete_activity():
    id = request.args.get('activity_id')
    activity = Activity.query.filter_by(id=id).first()
    activity.deleted = True
    db.session.add(activity)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_activity(Activity.get_current()),
                   result_del=format.format_del_activity(Activity.get_deleted()))

@backend.route('/delete/edu')
@login_required
def delete_edu():
    id = request.args.get('edu_id')
    edu = Edu.query.filter_by(id=id).first()
    edu.deleted = True
    db.session.add(edu)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_edu(Edu.get_current()),
                   result_del=format.format_del_edu(Edu.get_deleted()))
