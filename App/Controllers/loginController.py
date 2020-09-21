from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import request
from App import app
import os,os.path

# salvando com mesmo nome o arquivo é substituido

def AuthFinger():
    image = request.files['image']

    # permanece o nome original da imagem
    # filename = secure_filename(image.filename.rsplit('.', 1)[0])
    
    filename = 'image'
    ext = '.'+image.filename.rsplit('.', 1)[1]
    qtdArchives = str(len(os.listdir('Images')))

    print(filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename + qtdArchives + ext))
