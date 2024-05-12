# import cv2
# import os

# # Caminho para a pasta que contém as imagens
# path_to_images = '/home/getter-lab/Vídeos/video_1/bkp_crop/crop_1/'

# # Lista para armazenar as imagens
# images = []

# # Lê todas as imagens da pasta
# for filename in os.listdir(path_to_images):
#     if filename.endswith(".jpg") or filename.endswith(".png"): # Verifica se o arquivo é uma imagem
#         img = cv2.imread(os.path.join(path_to_images, filename))
#         if img is not None:
#             images.append(img)

# # Define a taxa de quadros do vídeo de saída
# fps = 1 # 1 frame a cada 7 segundos

# # Define o nome do arquivo de vídeo de saída
# output_video = '/home/getter-lab/Vídeos/video_1/bkp_crop/video.mp4'

# # Define o codec e cria o objeto VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec para MP4
# out = cv2.VideoWriter(output_video, fourcc, fps, (images[0].shape[1], images[0].shape[0]))

# # Escreve as imagens no arquivo de vídeo
# for i in range(len(images)):
#     out.write(images[i])
#     # Repete a imagem por 7 segundos
#     for _ in range(fps * 7 - 1): # Subtrai 1 porque já escrevemos a imagem uma vez
#         out.write(images[i])

# # Libera o objeto VideoWriter
# out.release()

from moviepy.editor import ImageClip, concatenate_videoclips
import os

# Caminho para a pasta onde estão as imagens
image_folder = '/home/getter-lab/Vídeos/video_1/bkp_crop/crop_1_N/'

# Lista de nomes de arquivos de imagem na ordem em que devem aparecer no vídeo
image_files = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))])

# Duração de cada imagem em segundos
duration = 1

# Lista para armazenar os clips de imagem redimensionados
clips = []

# Redimensiona cada imagem e adiciona ao clips
for image_file in image_files:
    clip = ImageClip(image_file, duration=duration)
    clip_resized = clip.resize(height=224) # Mantém a proporção de aspecto
    clips.append(clip_resized)

# Concatena todos os clips em um único clip
final_clip = concatenate_videoclips(clips, method="compose")

# Define o fps do final_clip
final_clip.fps = 1/duration # Ajuste conforme necessário

# Caminho e nome do arquivo de vídeo de saída
output_file = '/home/getter-lab/Vídeos/video_1/bkp_crop/video2.mp4'

# Escreve o clip final em um arquivo de vídeo
final_clip.write_videofile(output_file, codec='libx264')
