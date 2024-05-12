import os
import cv2
from groundingdino.util.inference import Model
from tqdm import tqdm

def main(
        image_directory: str = '',
        text_prompt: str = 'person',
        box_threshold: float = 0.15, 
        text_threshold: float = 0.10,
        export_dataset: bool = False,
        view_dataset: bool = False,
        export_annotated_images: bool = True,
        weights_path: str = "/home/getter-lab/GroundingDINO/weights/groundingdino_swint_ogc.pth",
        config_path: str = "/home/getter-lab/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
        subsample: int = None,
    ):
    # Carregar o modelo
    model = Model(model_config_path=config_path, model_checkpoint_path=weights_path)
    
    # Carregar os rótulos de classe
    classes = text_prompt.split(', ')
    
    # Função para Aprimorar Nomes de Classes
    def enhance_class_name(class_names):
        return [f"all {class_name}s" for class_name in class_names]
    
    # Função para Anotar Imagens em um Diretório no Formato KITTI
    def annotate_images_in_directory(directory):
        for class_name in classes:
            class_dir = os.path.join(directory, class_name)
            annotated_dir = os.path.join(directory, f"{class_name}_annotated")
            os.makedirs(annotated_dir, exist_ok=True)
            print(f"Processando imagens no diretório: {class_dir}")
            if os.path.isdir(class_dir):
                for image_name in tqdm(os.listdir(class_dir)):
                    image_path = os.path.join(class_dir, image_name)
                    image = cv2.imread(image_path)
                    if image is None:
                        print(f"Falha ao carregar a imagem: {image_path}")
                        continue
                    detections = model.predict_with_classes(
                        image=image,
                        classes=enhance_class_name([class_name]),
                        box_threshold=box_threshold,
                        text_threshold=text_threshold
                    )
                    # Salvar anotações no formato KITTI
                    kitti_annotations = []
                    for detection in detections:
                        kitti_line = f"{class_name} {detection.confidence} 0 -1 {detection.xmin} {detection.ymin} {detection.xmax} {detection.ymax} -1 -1 -1 -1 -1 -1 -1"
                        kitti_annotations.append(kitti_line)
                    # Salvar anotações no arquivo
                    kitti_filename = os.path.join(annotated_dir, f"{os.path.splitext(image_name)[0]}.txt")
                    with open(kitti_filename, "w") as kitti_file:
                        kitti_file.write("\n".join(kitti_annotations))
    
    # Anote imagens no diretório do conjunto de dados
    annotate_images_in_directory(image_directory)

# Exemplo de uso
if __name__ == "__main__":
    main(image_directory='test_grounding_dino', text_prompt='bus, car')
