import cv2
import numpy as np
import os

def resize_and_pad(img, size=352, pad_color=0):
    h, w = img.shape[:2]
    sh, sw = size, size

    # Interpolação
    if h > sh or w > sw:  # Reduzindo a imagem
        interp = cv2.INTER_AREA
    else:  # Ampliando a imagem
        interp = cv2.INTER_CUBIC

    # Proporção de aspecto da imagem
    aspect = w/h

    # Dimensionamento
    if aspect > 1:  # Imagem horizontal
        new_w = sw
        new_h = np.round(new_w / aspect).astype(int)
    elif aspect < 1:  # Imagem vertical
        new_h = sh
        new_w = np.round(new_h * aspect).astype(int)
    else:  # Imagem quadrada
        new_h, new_w = sh, sw

    # Redimensionar
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)

    # Calcula o preenchimento após o redimensionamento
    pad_vert = (sh - scaled_img.shape[0]) // 2
    pad_horz = (sw - scaled_img.shape[1]) // 2
    pad_top = pad_vert
    pad_bot = sh - scaled_img.shape[0] - pad_vert
    pad_left = pad_horz
    pad_right = sw - scaled_img.shape[1] - pad_horz

    # Cor do preenchimento
    if len(img.shape) == 3 and not isinstance(pad_color, (list, tuple, np.ndarray)):
        pad_color = [pad_color]*3

    # Adiciona preenchimento
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, cv2.BORDER_CONSTANT, value=pad_color)

    return scaled_img

# Caminho para a pasta com as imagens
folder_path = '/home/getter-lab/Vídeos/video_1/crop_test/'

# Lista todos os arquivos na pasta
files = os.listdir(folder_path)

for file in files:
    # Constrói o caminho completo do arquivo
    file_path = os.path.join(folder_path, file)
    
    # Carrega a imagem
    img = cv2.imread(file_path)
    
    # Verifica se a imagem foi carregada corretamente
    if img is not None:
        # Redimensiona e adiciona preenchimento à imagem
        resized_img = resize_and_pad(img)
        
        # Salva a imagem redimensionada
        cv2.imwrite(os.path.join(folder_path, f"resized_{file}"), resized_img)
