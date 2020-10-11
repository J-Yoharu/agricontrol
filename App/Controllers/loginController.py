from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import request
from App import app
import os,os.path

from PIL import Image as Image
import numpy as np
from skimage import color, img_as_float, exposure, filters


# salvando com mesmo nome o arquivo é substituido
digitalBd = ''

def AuthFinger(fingerUser):
    # imagem do usuário
    image = request.files['image']
    global digitalBd
    # imagem do banco de dados
    digitalBd = os.path.join(app.config['UPLOAD_FOLDER'],fingerUser)

    return fingerstandard(image)

def segmented_image(matrix):
    image = Image.open(matrix).resize((800,800))
    image2 = color.rgb2gray(img_as_float(image))
    image3 = exposure.equalize_hist(image2)

    segment_limit = filters.threshold_otsu(image3)

    matriz_segmented = []

    for value in image2:
        if image2.any() > segment_limit:
            matriz_segmented.append(value)
    matrix_Segment = np.array(matriz_segmented)

    return matrix_Segment

def fingerstandard(image):
    finger1 = segmented_image(image)

    result = mse(finger1)

    return result

def mse(array):
        global digitalBd

        finger_normalized = segmented_image(digitalBd) # CHAMANDO NOVAMENTE A FUNÇÃO PARA SEGMENTAR A IMAGEM DO BANCO DE DADOS

        result3 = ((array - finger_normalized) ** 2) # REALIZANDO A COMPARAÇÃO MSE

        # Com o array normalizado ficou mais claro se o acesso será permitido ou não, pois
        # se a digital for a mesma o resultado será zero, caso contrario sera um erro de quase 30% aproximadamente
        if result3.mean() <= 0.03:
            print(result3.mean())
            print("Acesso permitido, seja bem vindo ")
            return True
        else:
            print("Sem Correspondência")
            return False

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
    imageName = filename + qtdArchives + ext
    image.save(os.path.join(folder , imageName))
    return imageName