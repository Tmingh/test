import os, hashlib, json
from . import backend
from flask import redirect, url_for, request, current_app, jsonify
from .. import db
from datetime import datetime
from ..models import Project, Maker, Edu, Activity, Label, Video, Banner, HandpickedMaker, HandpickedProject
from flask_login import login_required

def save_image(file):
    md5 = hashlib.md5()
    filename = file.filename
    fname, fext = os.path.splitext(file.filename)
    md5.update(fname.encode('utf-8'))
    hashname = '%s%s' % (md5.hexdigest(), fext)
    filepath = os.path.join(current_app.static_folder, 'upload', hashname)
    dirName = os.path.dirname(filepath)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    file.save(filepath)
    url = '/%s/%s/%s' % ('static', 'upload', hashname)
    return url

@backend.route('/add/project', methods=['POST', 'GET'])
@login_required
def add_project():
    if request.method == 'POST':
        labels = request.form.getlist('labels')
        need_money = False
        need_partners = False
        need_devices = False
        name, managerName = request.form['proj_name'], request.form['proj_manager_name']
        managerInfo, email = request.form['proj_manager_info'], request.form['proj_email']
        proj_sum = request.form['proj_sum']
        image = save_image(request.files['proj_image'])
        introduction = request.form['proj_introduction']
        teacher = request.form['proj_teacher']
        if 'need_money' in request.form and request.form['need_money'] == 'on':
            need_money = True
        if 'need_partners' in request.form and request.form['need_partners'] == 'on':
            need_partners = True
        if 'need_devices' in request.form and request.form['need_devices'] == 'on':
            need_devices = True
        new_project = Project(name=name, mgr_name=managerName, mgr_info=managerInfo, image_url=image,
                              email=email, sum=proj_sum, introduction=introduction, need_money=need_money,
                              need_partners=need_partners, need_devices=need_devices, teacher=teacher,
                              submit_time=datetime.now())
        for label_id in labels:
            label = Label.query.filter_by(id=int(label_id)).first()
            new_project.labels.append(label)
        db.session.add(new_project)
        db.session.commit()
    return redirect(url_for('backend.backend_index',
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
                            hp_makers=[Maker.query.filter_by(id=hp_maker.maker_id).first() for hp_maker in HandpickedMaker.query.all()]))

@backend.route('/add/maker', methods=['POST'])
@login_required
def add_maker():
    name, info = request.form['maker_name'], request.form['maker_info']
    sum, introduction = request.form['maker_sum'], request.form['maker_introduction']
    image = save_image(request.files['maker_image'])
    new_maker = Maker(name=name, image_url=image, info=info,
                      sum=sum, introduction=introduction, submit_time=datetime.now())
    db.session.add(new_maker)
    db.session.commit()
    return redirect(url_for('backend.backend_index',
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
                            hp_makers=[Maker.query.filter_by(id=hp_maker.maker_id).first() for hp_maker in HandpickedMaker.query.all()]))

@backend.route('/add/activity', methods=['POST'])
@login_required
def add_activity():
    name, sponsor = request.form['activity_name'], request.form['activity_sponsor']
    sum, introduction = request.form['activity_sum'], request.form['activity_introduction']
    image_url = save_image(request.files['activity_image'])
    enroll_url = save_image(request.files['activity_enroll'])
    new_activity = Activity(name=name, sponsor=sponsor, sum=sum, submit_time=datetime.now(),
                            introduction=introduction, image_url=image_url, enroll_url=enroll_url)
    db.session.add(new_activity)
    db.session.commit()
    return redirect(url_for('backend.backend_index',
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
                            hp_makers=[Maker.query.filter_by(id=hp_maker.maker_id).first() for hp_maker in HandpickedMaker.query.all()]))

@backend.route('/add/edu', methods=['POST'])
@login_required
def add_edu():
    name = request.form['edu_name']
    sum = request.form['edu_sum']
    speaker = request.form['edu_speaker']
    video_names = request.form.getlist('video_name')
    video_urls = request.form.getlist('video_url')
    image = save_image(request.files['edu_image'])
    new_edu = Edu(name=name, sum=sum, speaker=speaker, image_url=image, submit_time=datetime.now())
    index = 0
    while index < len(video_urls):
        video = Video(name=video_names[index], url=video_urls[index])
        new_edu.videos.append(video)
        index += 1
    db.session.add(new_edu)
    db.session.commit()
    return redirect(url_for('backend.backend_index',
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
                            hp_makers=[Maker.query.filter_by(id=hp_maker.maker_id).first() for hp_maker in HandpickedMaker.query.all()]
                            ))
