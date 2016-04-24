from . import main
from flask import jsonify, request, render_template
from ..models import Maker

def maker_orm_to_dict(orm):
    dict = {
        'id': orm.id,
        'name': orm.name,
        'image_url': orm.image_url,
        'info': orm.info,
        'sum': orm.sum,
        'introduction': orm.introduction
    }

    return dict

@main.route('/maker', methods=['GET', 'POST'])
def main_maker():
    if request.method == 'POST':
        latest_maker_orm = Maker.query.order_by(Maker.submit_time.desc()).all()
        latest_maker_dict = [maker_orm_to_dict(orm) for orm in latest_maker_orm]

        result = {
            'latest_maker': latest_maker_dict,
        }
        return jsonify(result=result)
    return render_template('main_maker.html')

@main.route('/maker/<int:id>', methods=['GET', 'POST'])
def solo_maker(id):
    if request.method == 'POST':
        maker = Maker.query.filter_by(id=id).first_or_404()
        return jsonify(result=maker_orm_to_dict(maker))
    return render_template('solo_maker.html')
