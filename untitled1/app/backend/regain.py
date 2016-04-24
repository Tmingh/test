from flask import redirect, url_for, jsonify, request
from flask_login import login_required
from . import backend, format
from .. import db
from ..models import Project, Maker, Edu, Activity

@backend.route('/regain/proj')
@login_required
def regain_proj():
    id = request.args.get('proj_id')
    proj = Project.query.filter_by(id=id).first()
    proj.deleted = False
    db.session.add(proj)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_proj(Project.get_current()),
                   result_del=format.format_del_proj(Project.get_deleted()))

@backend.route('/regain/maker')
@login_required
def regain_maker():
    id = request.args.get('maker_id')
    maker = Maker.query.filter_by(id=id).first()
    maker.deleted = False
    db.session.add(maker)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_maker(Maker.get_current()),
                   result_del=format.format_del_maker(Maker.get_deleted()))

@backend.route('/regain/activity')
@login_required
def regain_activity():
    id = request.args.get('activity_id')
    activity = Activity.query.filter_by(id=id).first()
    activity.deleted = False
    db.session.add(activity)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_activity(Activity.get_current()),
                   result_del=format.format_del_activity(Activity.get_deleted()))

@backend.route('/regain/edu')
@login_required
def regain_edu():
    id = request.args.get('edu_id')
    edu = Edu.query.filter_by(id=id).first()
    edu.deleted = False
    db.session.add(edu)
    db.session.commit()

    return jsonify(result_cur=format.format_cur_edu(Edu.get_current()),
                   result_del=format.format_del_edu(Edu.get_deleted()))
