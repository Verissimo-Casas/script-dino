import os

def main():
    labels_dir = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/image_2'
    images_dir = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/label_2'
    
    
    # Lista todos os arquivos .png no diretório de imagens
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    
    for image_file in image_files:
        # Obtém o nome do arquivo sem a extensão
        base_name = os.path.splitext(image_file)[0]
        # Define o caminho do arquivo de texto correspondente
        txt_path = os.path.join(labels_dir, base_name + ".txt")
        
        # Verifica se o arquivo de texto correspondente existe
        if not os.path.exists(txt_path):
            print(f"Arquivo de texto correspondente não encontrado para {image_file}")

if __name__ == "__main__":
    main()
