from . import main
from flask import jsonify, request, render_template, url_for
from ..models import Label, Project

def proj_orm_to_dict(orm):
    dict = {
            'id': orm.id,
            'name': orm.name,
            'likes': orm.likes,
            'image_url': orm.image_url,
            'mgr_name': orm.mgr_name,
            'mgr_info': orm.mgr_info,
            'teacher': orm.teacher,
            'email': orm.email,
            'sum': orm.sum,
            'url': url_for('main.solo_project', id=orm.id),
            'introduction': orm.introduction,
            'need_money': orm.need_money,
            'need_partners': orm.need_partners,
            'need_devices': orm.need_devices
    }

    return dict

@main.route('/project', methods=['GET', 'POST'])
def main_project():
    if request.method == 'POST':
        labels = Label.query.order_by(Label.id)
        labels_num = [label.projects.count() for label in labels]
        for label in labels:
            print(label.projects.count())
        latest_project_orm = Project.query.order_by(Project.submit_time.desc()).all()
        hottest_project_orm = Project.query.order_by(Project.likes.desc()).all()
        latest_project_dict = [proj_orm_to_dict(orm) for orm in latest_project_orm]
        hottest_project_dict = [proj_orm_to_dict(orm) for orm in hottest_project_orm]
        return jsonify(labels_num=labels_num, new_projects=latest_project_dict, hot_projects=hottest_project_dict)
    return render_template('main_project.html')

@main.route('/project/<id>', methods=['GET', 'POST'])
def solo_project(id):
    if request.method == 'POST':
        project = Project.query.filter_by(id=int(id)).first_or_404()
        return jsonify(project=proj_orm_to_dict(project))
    return render_template('solo_project.html', id=id)

@main.route('/project/labels/<id>', methods=['GET', 'POST'])
def label_project(id):
    if request.method == 'POST':
        label = Label.query.filter_by(id=int(id)).first_or_404()
        dict_label = {
            'name': label.name
        }
        orm_project = label.projects
        dict_project = [proj_orm_to_dict(orm) for orm in orm_project]
        return jsonify(projects=dict_project, label=dict_label)
    return render_template('label_project.html', id=int(id))
