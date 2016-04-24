import os, xlwt, xlrd, datetime, hashlib, re, json
from flask import render_template, request, jsonify, url_for, redirect, current_app, flash, send_from_directory
from flask_login import login_required
from . import backend
from .. import db
from ..models import Project, Maker, Edu, Activity, Label, Banner, HandpickedMaker, HandpickedProject

md5 = hashlib.md5()

@backend.route('/', methods=['GET', 'POST'])
@login_required
def backend_index():
    # temp = Project.query.order_by(Project.submit_time.desc()).all()
    # output = []
    # for project in temp:
    #     a = {
    #         'id': project.id,
    #         'name': project.name,
    #         'image_url': project.image_url,
    #         'mgr_name': project.mgr_name,
    #         'mgr_info': project.mgr_info,
    #         'teacher': project.teacher,
    #         'email': project.email,
    #         'sum': project.sum,
    #         'introduction': project.introduction,
    #         'need_money': project.need_money,
    #         'need_partners': project.need_partners,
    #         'need_devices': project.need_devices
    #     }
    #     output.append(a)
    #
    # print(json.dumps(output))
    print(url_for('backend.add_edu'))
    return render_template('index.html',
                           current_projects=Project.get_current(),
                           deleted_projects=Project.get_deleted(),
                           current_makers=Maker.get_current(),
                           deleted_makers=Maker.get_deleted(),
                           current_activities=Activity.get_current(),
                           deleted_activities=Activity.get_deleted(),
                           current_edus=Edu.get_current(),
                           deleted_edus=Edu.get_deleted(),
                           banners=Banner.query.all(),
                           hp_projects=[Project.query.filter_by(id=hp_project.project_id).first() for hp_project in HandpickedProject.query.all()],
                           hp_makers=[Maker.query.filter_by(id=hp_maker.maker_id).first() for hp_maker in HandpickedMaker.query.all()])
