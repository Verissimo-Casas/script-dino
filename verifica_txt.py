import os

pasta_imagens = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/image_2'
pasta_labels = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/label_2'

# Obter a lista de arquivos de imagens e rótulos
imagens = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]
labels = [f for f in os.listdir(pasta_labels) if f.endswith('.txt')]

# Encontrar arquivos sem correspondência
imagens_sem_correspondencia = [imagem for imagem in imagens if imagem.replace(".png", ".txt") not in labels]
labels_sem_correspondencia = [label for label in labels if label.replace(".txt", ".png") not in imagens]

# Remover arquivos sem correspondência
for imagem in imagens_sem_correspondencia:
    caminho_imagem = os.path.join(pasta_imagens, imagem)
    os.remove(caminho_imagem)
    print(f"Removido: {caminho_imagem}")

for label in labels_sem_correspondencia:
    caminho_label = os.path.join(pasta_labels, label)
    os.remove(caminho_label)
    print(f"Removido: {caminho_label}")

print("Processo de validação e remoção concluído.")
