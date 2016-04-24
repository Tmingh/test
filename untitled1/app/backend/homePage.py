from . import backend
from .. import db
from flask import jsonify, request, redirect, url_for
from ..models import Banner, HandpickedProject, HandpickedMaker, Project, Maker
from .add import save_image
from .format import format_banner, format_hp_project, format_hp_maker

@backend.route('/change/banners')
def change_banners():
    banners_str = request.args.getlist('banners_submit[]')
    banners = [Banner.query.filter_by(id=int(n)).first() for n in banners_str]
    i = 1
    for banner in banners:
        banner.number = i
        i += 1
    db.session.add_all(banners)
    db.session.commit()

    return jsonify(response='修改成功')

@backend.route('/change/handpicked/project')
def change_hp_projects():
    hp_projects_str = request.args.getlist('hp_projects_submit[]')
    hp_projects = [HandpickedProject.query.filter_by(id=int(n)).first() for n in hp_projects_str]
    i = 1
    for hp_project in hp_projects:
        hp_project.number = i
        i += 1
    db.session.add_all(hp_projects)
    db.session.commit()

    return jsonify(response='修改成功')

@backend.route('/change/handpicked/maker')
def change_hp_makers():
    hp_makers_str = request.args.getlist('hp_makers_submit[]')
    hp_makers = [HandpickedMaker.query.filter_by(id=int(n)).first() for n in hp_makers_str]
    i = 1
    for hp_maker in hp_makers:
        hp_makers.number = i
        i += 1
    db.session.add_all(hp_makers)
    db.session.commit()

    return jsonify(response='修改成功')

@backend.route('/add/handpicked/project')
def add_proj_to_homepage():
    number = 1
    id = request.args.get('proj_id')
    project = Project.query.filter_by(id=int(id)).first()
    if HandpickedProject.query.filter_by(project_id=project.id).first() is not None:
        return jsonify(response='添加失败：项目已添加')
    if HandpickedProject.query.filter_by(project_id=project.id).count() > 4:
        return jsonify(response='添加失败：精选数已满，请删除后在进行添加')
    if project is None:
        return jsonify(response='添加失败：项目不存在')
    last_hp_project = HandpickedProject.query.order_by(HandpickedProject.number.desc()).first()
    if last_hp_project is not None:
        number = last_hp_project.number + 1
    new_hp_project = HandpickedProject(project_id=project.id, number=number)
    db.session.add(new_hp_project)
    db.session.commit()

    return jsonify(response='添加成功')

@backend.route('/add/handpicked/maker')
def add_maker_to_homepage():
    number = 1
    id = request.args.get('maker_id')
    maker = Maker.query.filter_by(id=int(id)).first()
    if HandpickedMaker.query.filter_by(maker_id=maker.id).first() is not None:
        return jsonify(response='添加失败：项目已添加')
    if HandpickedMaker.query.filter_by(maker_id=maker.id).count() > 4:
        return jsonify(response='添加失败：精选数已满，请删除后在进行添加')
    if maker is None:
        return jsonify(response='添加失败：项目不存在')
    last_hp_maker = HandpickedMaker.query.order_by(HandpickedMaker.number.desc()).first()
    if last_hp_maker is not None:
        number = last_hp_maker.number + 1
    new_hp_maker = HandpickedMaker(maker_id=maker.id, number=number)
    db.session.add(new_hp_maker)
    db.session.commit()

    return jsonify(response='添加成功')

@backend.route('/add/banner', methods=['GET', 'POST'])
def add_banner():
    number = 1
    image_url = save_image(request.files['banner_image'])
    target_url = request.form['banner_target']
    last_banner = Banner.query.order_by(Banner.number.desc()).first()
    if last_banner is not None:
        number = last_banner.number + 1
    new_banner = Banner(image_url=image_url, target_url=target_url, number=number)
    db.session.add(new_banner)
    db.session.commit()
    
    return redirect(url_for('backend.index'))

@backend.route('/delete/banner')
def delete_banner():
    id = request.args.get('banner_id')
    deleted_banner = Banner.query.filter_by(id=int(id)).first()
    db.session.delete(deleted_banner)
    db.session.commit()
    banners = Banner.query.all()
    for banner in banners:
        if banner.number < int(id):
            banner.number -= 1
    db.session.add_all(banners)
    db.session.commit()

    return jsonify(result=format_banner(Banner.query.all()))

@backend.route('/delete/handpicked/project')
def delete_hp_project():
    id = request.args.get('hp_project_id')
    deleted_hp_project = HandpickedProject.query.filter_by(project_id=int(id)).first()
    db.session.delete(deleted_hp_project)
    db.session.commit()
    hp_projects = HandpickedProject.query.all()
    for hp_project in hp_projects:
        if hp_project.number < int(id):
            hp_project.number -= 1
    db.session.add_all(hp_projects)
    db.session.commit()

    return jsonify(result=format_hp_project(HandpickedProject.query.all()))

@backend.route('/delete/handpicked/maker')
def delete_hp_maker():
    id = request.args.get('hp_maker_id')
    deleted_hp_maker = HandpickedMaker.query.filter_by(maker_id=int(id)).first()
    db.session.delete(deleted_hp_maker)
    db.session.commit()
    hp_makers = HandpickedMaker.query.all()
    for hp_maker in hp_makers:
        if hp_maker.number < int(id):
            hp_maker.number -= 1
    db.session.add_all(hp_makers)
    db.session.commit()

    return jsonify(result=format_hp_maker(HandpickedMaker.query.all()))

