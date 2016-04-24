from flask import Blueprint, request, url_for, jsonify
import datetime, random, os

upload = Blueprint('upload', __name__)

def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@upload.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'fileData' in request.files:
        data = {}
        error = ''
        url = ''
        fileobj = request.files['fileData']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(upload.static_folder, 'upload', rnd_name)
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'
        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
            data = {
            'success': True,
            'msg': '',
            'file_path': url
            }
    return jsonify(data)
