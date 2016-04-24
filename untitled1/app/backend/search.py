import re
from . import backend, format
from flask import redirect, url_for, request, flash, jsonify
from flask_login import login_required
from .. import db
from ..models import Project, Maker, Edu, Activity

@backend.route('/search/proj')
@login_required
def search_proj():
    type = request.args.get('type')
    target = request.args.get('target')
    key = request.args.get('key')
    if key == '请输入搜索内容':
        if target == 'current':
            return jsonify(result=format.format_cur_proj(Project.get_current()))
        elif target == 'deleted':
            return jsonify(result=format.format_del_proj(Project.get_deleted()))
    temp = '.*?('+key+').*?'
    key_re = re.compile(temp.encode('utf8'))
    projects = []
    results = []
    if target == 'current':
        projects = Project.get_current()
    elif target == 'deleted':
        projects = Project.get_deleted()
    if type == 'tag':
        for project in projects:
            for label in project.labels:
                if re.match(key_re, label.encode('utf8')):
                    results.append(project)
    elif type == 'name':
        for project in projects:
            name = project.name
            if re.match(key_re, name.encode('utf8')):
                results.append(project)

    if target == 'current':
        return jsonify(result=format.format_cur_proj(results))
    elif target == 'deleted':
        return jsonify(result=format.format_del_proj(results))

@backend.route('/search/maker')
@login_required
def search_maker():
    target = request.args.get('target')
    key = request.args.get('key')
    if key == '请输入搜索内容':
        if target == 'current':
            return jsonify(result=format.format_cur_maker(Maker.get_current()))
        elif target == 'deleted':
            return jsonify(result=format.format_del_maker(Maker.get_deleted()))

    temp = '.*?('+key+').*?'
    key_re = re.compile(temp.encode('utf8'))
    makers = []
    results = []
    if target == 'current':
        makers = Maker.get_current()
    elif target == 'deleted':
        makers = Maker.get_deleted()
    for maker in makers:
        if re.match(key_re, maker.name.encode('utf8')):
            results.append(maker)

    if target == 'current':
        return jsonify(result=format.format_cur_maker(results))
    elif target == 'deleted':
        return jsonify(result=format.format_del_maker(results))

@backend.route('/search/activity')
@login_required
def search_activity():
    target = request.args.get('target')
    key = request.args.get('key')
    if key == '请输入搜索内容':
        if target == 'current':
            return jsonify(result=format.format_cur_activity(Activity.get_current()))
        elif target == 'deleted':
            return jsonify(result=format.format_del_activity(Activity.get_deleted()))
    temp = '.*?('+key+').*?'
    key_re = re.compile(temp.encode('utf8'))
    activities = []
    results = []
    if target == 'current':
        activities = Activity.get_current()
    elif target == 'deleted':
        activities = Activity.get_deleted()
    for activity in activities:
        if re.match(key_re, activity.name.encode('utf8')):
            results.append(activity)

    if target == 'current':
        return jsonify(result=format.format_cur_activity(results))
    elif target == 'deleted':
        return jsonify(result=format.format_del_activity(results))

@backend.route('/search/edu')
@login_required
def search_edu():
    target = request.args.get('target')
    key = request.args.get('key')
    if key == '请输入搜索内容':
        if target == 'current':
            return jsonify(result=format.format_cur_edu(Edu.get_current()))
        elif target == 'deleted':
            return jsonify(result=format.format_del_edu(Edu.get_deleted()))
    temp = '.*?('+key+').*?'
    key_re = re.compile(temp.encode('utf8'))
    edus = []
    results = []
    if target == 'current':
        edus = Edu.get_current()
    elif target == 'deleted':
        edus = Edu.get_deleted()
    for edu in edus:
        if re.match(key_re, edu.name.encode('utf8')):
            results.append(edu)

    if target == 'current':
        return jsonify(result=format.format_cur_edu(results))
    elif target == 'deleted':
        return jsonify(result=format.format_del_edu(results))
