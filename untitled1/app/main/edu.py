from . import main
from flask import jsonify, render_template, request
from ..models import Edu

def edu_orm_to_dict(orm):
    videos = [video.url for video in orm.videos]
    dict = {
        'id': orm.id,
        'name': orm.name,
        'image_url': orm.image_url,
        'speaker': orm.speaker,
        'sum': orm.sum,
        'videos': videos
    }

    return dict

@main.route('/edu', methods=['GET', 'POST'])
def main_edu():
    if request.method == 'POST':
        latest_edu_orm = Edu.query.order_by(Edu.submit_time.desc()).all()
        latest_edu_dict = [edu_orm_to_dict(orm) for orm in latest_edu_orm]

        result = {
            'latest_edu': latest_edu_dict,
        }
        return jsonify(result=result)
    return render_template('main_edu.html')

@main.route('/edu/<int:id>', methods=['GET', 'POST'])
def solo_edu(id):
    if request.method == 'POST':
        edu = Edu.query.filter_by(id=id).first_or_404()
        return jsonify(result=edu_orm_to_dict(edu))
    return render_template('solo_edu.html')
