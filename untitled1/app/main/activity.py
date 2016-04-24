from . import main
from flask import jsonify, render_template, request
from ..models import Activity

def activity_orm_to_dict(orm):
    dict = {
        'id': orm.id,
        'name': orm.name,
        'image_url': orm.image_url,
        'sponsor': orm.sponsor,
        'sum': orm.sum,
        'introduction': orm.introduction,
        'enroll_url': orm.enroll_url
    }

    return dict

@main.route('/activity', methods=['GET', 'POST'])
def main_activity():
    if request.method == 'POST':
        latest_activity_orm = Activity.query.order_by(Activity.submit_time.desc()).all()
        latest_activity_dict = [activity_orm_to_dict(orm) for orm in latest_activity_orm]

        result = {
            'latest_activity': latest_activity_dict,
        }
        return jsonify(result=result)
    return render_template('main_activity.html')

@main.route('/activity/<int:id>', methods=['GET', 'POST'])
def solo_activity(id):
    if request.method == 'POST':
        activity = Activity.query.filter_by(id=id).first_or_404()
        return jsonify(result=activity_orm_to_dict(activity))
    return render_template('solo_activity.html')
