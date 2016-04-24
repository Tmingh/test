from flask import url_for
from ..models import Project, Maker

def format_cur_proj(projects):
    rs = ''
    for project in projects:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_proj(%d, 0)"> 删除</a>' \
               '<a href="#" onclick="delete_proj(%d, 1)"> 彻底删除</a>' \
               '<a href="#" onclick="add_proj_to_homepage(%d)"> 添加至首页</a>' \
               '</td>' \
               '</tr>' % (project.name, project.mgr_name,project.mgr_info,
                          project.teacher, url_for('main.solo_project', id=project.id),
                          project.id, project.id, project.id)
        rs += temp
    return rs

def format_del_proj(projects):
    rs = ''
    for project in projects:
            temp = '<tr>' \
                   '<td>%s</td>' \
                   '<td>%s</td>' \
                   '<td>%s</td>' \
                   '<td>%s</td>' \
                   '<td><a href="%s">点击查看</a></td>' \
                   '<td>' \
                   '<a href="#" onclick="delete_proj(%d, 1)"> 彻底删除</a>' \
                   '<a href="#" onclick="regain_proj(%d)"> 恢复</a>' \
                   '</td>' \
                   '</tr>' % (project.name, project.mgr_name, project.mgr_info,
                              project.teacher, url_for('main.solo_project', id=project.id),
                              project.id, project.id)
            rs += temp
    return rs

def format_cur_maker(makers):
    rs = ''
    for maker in makers:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_maker(%d, 0)"> 删除</a>' \
               '<a href="#" onclick="delete_maker(%d, 1)"> 彻底删除</a>' \
               '<a href="#" onclick="add_maker_to_homepage(%d)"> 添加至首页</a>' \
               '</td>' \
               '</tr>' % (maker.name, maker.info, url_for("main.solo_maker", id=maker.id),
                          maker.id, maker.id, maker.id)
        rs += temp
    return rs

def format_del_maker(makers):
    rs = ''
    for maker in makers:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_maker(%d, 1)"> 彻底删除</a>' \
               '<a href="#" onclick="regain_maker(%d)"> 恢复</a>' \
               '</td>' \
               '</tr>' % (maker.name, maker.info, url_for("main.solo_maker", id=maker.id),
                          maker.id, maker.id)
        rs += temp
    return rs

def format_cur_activity(activities):
    rs = ''
    for activity in activities:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_activity(%d, 0)"> 删除</a>' \
               '<a href="#" onclick="delete_activity(%d, 1)"> 彻底删除</a>' \
               '</td>' \
               '</tr>' % (activity.name, activity.sponsor,
                          url_for("main.solo_activity", id=activity.id),
                          activity.id, activity.id)
        rs += temp
    return rs

def format_del_activity(activities):
    rs = ''
    for activity in activities:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_activity(%d, 1)"> 彻底删除</a>' \
               '<a href="#" onclick="regain_activity(%d)"> 恢复</a>' \
               '</td>' \
               '</tr>' % (activity.name, activity.sponsor,
                          url_for("main.solo_activity", id=activity.id),
                          activity.id, activity.id)
        rs += temp
    return rs

def format_cur_edu(edus):
    rs = ''
    for edu in edus:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_edu({%d, 0)"> 删除</a>' \
               '<a href="#" onclick="delete_edu(%d, 1)"> 彻底删除</a>' \
               '</td>' \
               '</tr>' % (edu.name, edu.speaker,
                          url_for("main.solo_edu", id=edu.id),
                          edu.id, edu.id)
        rs += temp
    return rs

def format_del_edu(edus):
    rs = ''
    for edu in edus:
        temp = '<tr>' \
               '<td>%s</td>' \
               '<td>%s</td>' \
               '<td><a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a href="#" onclick="delete_edu(%d, 1)"> 彻底删除</a>' \
               '<a href="#" onclick="regain_edu(%d)"> 恢复</a>' \
               '</td>' \
               '</tr>' % (edu.name, edu.speaker,
                          url_for("main.solo_edu", id=edu.id),
                          edu.id, edu.id)
        rs += temp
    return rs

def format_banner(banners):
    rs = ''
    for banner in banners:
        temp = '<tr num="%d">' \
               '<td>%d</td><td>' \
               '<a href="%s">点击查看</a></td>' \
               '<td>' \
               '<a onclick="moveUp(this)" href="#"> 上移</a>' \
               '<a onclick="moveDown(this)" href="#"> 下移</a>' \
               '<a href="#" onclick="delete_banner(%d)"> 删除</a>' \
               '</td>' \
               '</tr>' % (banner.id, banner.number, banner.target_url, banner.id)
        rs += temp
    return rs

def format_hp_project(hp_projects):
    rs = ''
    for hp_project in hp_projects:
        project = Project.query.filter_by(id=hp_project.project_id).first()
        temp = '<tr num="%d">' \
               '<td>%s</td>' \
               '<td>' \
               '<a href="#">点击查看</a>' \
               '</td>' \
               '<td>' \
               '<a onclick="moveUp(this)" href="#"> 上移</a>' \
               '<a onclick="moveDown(this)" href="#"> 下移</a>' \
               '<a href="#" onclick="delete_hp_project(%d)"> 删除</a>' \
               '</td>' \
               '</tr>' %(project.id, project.name, project.id)
        rs += temp
    return rs

def format_hp_maker(hp_makers):
    rs = ''
    for hp_maker in hp_makers:
        maker = Maker.query.filter_by(id=hp_maker.maker_id).first()
        temp = '<tr num="%d">' \
               '<td>%s</td>' \
               '<td>' \
               '<a href="#">点击查看</a>' \
               '</td>' \
               '<td>' \
               '<a onclick="moveUp(this)" href="#"> 上移</a>' \
               '<a onclick="moveDown(this)" href="#"> 下移</a>' \
               '<a href="#" onclick="delete_hp_maker(%d)"> 删除</a>' \
               '</td>' \
               '</tr>' %(maker.id, maker.name, maker.id)
        rs += temp
    return rs
