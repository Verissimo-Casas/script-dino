import cv2
import os

def crop_images_from_labels(image_folder, label_folder, output_folder):
    # Verifica se a pasta de saída existe, caso não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lista todas as imagens no diretório de imagens
    list_of_images = os.listdir(image_folder)
    
    # Itera sobre cada imagem
    for image_name in list_of_images:
        # Caminho completo para a imagem
        image_path = os.path.join(image_folder, image_name)
        
        # Caminho para o arquivo de etiquetas correspondente
        label_path = os.path.join(label_folder, image_name[:-4] + '.txt')
        
        # Carrega a imagem
        img = cv2.imread(image_path)
        
        # Abre e lê o arquivo de etiquetas
        with open(label_path, 'r') as file:
            lines = file.readlines()
        
        # Itera sobre cada linha do arquivo de etiquetas
        for line in lines:
            # Dividir a linha em componentes
            parts = line.strip().split(' ')
            
            # Obter as coordenadas do retângulo de delimitação
            # As coordenadas são: x_min, y_min, x_max, y_max
            x_min, y_min, x_max, y_max = map(lambda x: int(float(x)), parts[4:8])
            
            # Recortar a imagem usando as coordenadas
            cropped_img = img[y_min:y_max, x_min:x_max]
            
            # Salvar a imagem recortada no diretório de saída
            output_path = os.path.join(output_folder, image_name[:-4] + '.png')
            cv2.imwrite(output_path, cropped_img)

# Exemplo de uso
image_folder = '/home/getter-lab/Vídeos/video_1/images/' # Substitua pelo caminho da sua pasta de imagens
label_folder = '/home/getter-lab/Vídeos/video_1/labels/' # Substitua pelo caminho da sua pasta de etiquetas
output_folder = '/home/getter-lab/Vídeos/video_1/crop_7/' # Substitua pelo caminho onde você deseja salvar as imagens recortadas

crop_images_from_labels(image_folder, label_folder, output_folder)
