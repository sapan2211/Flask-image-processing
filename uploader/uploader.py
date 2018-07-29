from flask import Flask, render_template, request
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/uploader/files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader',methods = ['POST', 'GET'])
def uploader():
   if request.method == 'POST':
       file = request.files['file']
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run("0.0.0.0",80,debug = True)

