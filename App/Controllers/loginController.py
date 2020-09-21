from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import request
from App import app
import os,os.path

# salvando com mesmo nome o arquivo é substituido

def AuthFinger(fingerUser):
    image = request.files['image']

    folder = app.config['UPLOAD_FOLDER']
    filename = 'fingerTemp'
    ext = '.'+image.filename.rsplit('.', 1)[1]

    image.save(os.path.join(folder , filename + ext))
    print(fingerUser)
    print(filename+ext)
    return True
    
def Register():
    image = request.files['image']
    # os.path pega o caminho absoluto para a pasta
    # permanece o nome original da imagem
    # filename = secure_filename(image.filename.rsplit('.', 1)[0])
    folder = app.config['UPLOAD_FOLDER']
    filename = 'image'
    ext = '.'+image.filename.rsplit('.', 1)[1]
    qtdArchives = str(len(os.listdir('Images')))

    print(filename)
    image.save(os.path.join(folder , filename + qtdArchives + ext))