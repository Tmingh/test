import os
from flask import request, Response, current_app, url_for
from flask_login import login_required
from . import backend

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@backend.route("/ImageUpdate", methods=["POST"])
# @login_required
def GetImage():
    if request.method == 'POST':
        file = None
        if request.files['wangEditorH5File']:
            file = request.files['wangEditorH5File']
        elif request.files['wangEditorFormFile']:
            file = request.files['wangEditorFormFile']
        elif request.files['wangEditorPasteFile']:
            file = request.files['wangEditorPasteFile']
        elif request.files['wangEditorDragFile']:
            file = request.files['wangEditorDragFile']
        if file == None:
            result = r"error|未成功获取文件，上传失败"
            res = Response(result)
            res.headers["ContentType"] = "text/html"
            res.headers["Charset"] = "utf-8"
            return res
        else:
            if file and allowed_file(file.filename):
                filename = file.filename
                print('upload/'+filename)
                filepath = os.path.join(current_app.static_folder, 'upload', filename)
                dirName = os.path.dirname(filepath)
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                file.save(filepath)
                res = Response(url_for('static', filename='%s/%s' % ('upload', filename)))
                print(url_for('static', filename='%s/%s' % ('upload', filename)))
                res.headers["ContentType"] = "text/html"
                res.headers["Charset"] = "utf-8"
                return res
