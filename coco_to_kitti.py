import os
import shutil
from pycocotools.coco import COCO


def crear_y_mover_directorio(origen, nombre_destino):
    # Crear el directorio de destino dentro del directorio de origen
    destino = os.path.join(origen, nombre_destino)
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Mover todos los archivos del directorio de origen al directorio de destino
    for archivo in os.listdir(origen):
        origen_path = os.path.join(origen, archivo)
        destino_path = os.path.join(destino, archivo)
        if os.path.isfile(origen_path):  # Verificar que sea un archivo y no un directorio
            shutil.copy(origen_path, destino_path)


def coco2kitti(catNms, annFile):
    """
    Converts annotations in COCO format to a custom KITTI format.

    Parameters:
    - catNms (list): List of category names to include in KITTI tags.
    - annFile (str): Path to the COCO annotation JSON file.

    Returns:
    None
    """

    # Initialize the COCO API for instance annotations
    coco = COCO(annFile)

    # Create an index for category names
    cats = coco.loadCats(coco.getCatIds())
    
    cat_idx = {}
    for c in cats:
        cat_idx[c['id']] = c['name']
        print(cat_idx[c['id']])

    # Iterate over all images in the COCO dataset
    for img in coco.imgs:

        # Get all annotation IDs for the image
        catIds = coco.getCatIds(catNms=catNms)
        
        annIds = coco.getAnnIds(imgIds=[img], catIds=catIds)
        
        # If there are annotations, create a tag file
        if len(annIds) > 0:
            # Get the file name of the image
            img_fname = coco.imgs[img]['file_name']
            
            # Open the text file
            #with open(destination_labels + img_fname[:-4] + '.txt', 'w') as label_file:
            with open('/home/getter-lab/Vídeos/video_1/labels/' + img_fname[:-4] + '.txt', 'w') as label_file:
                anns = coco.loadAnns(annIds)
                print(anns)
                for a in anns:
                    
                    bbox = a['bbox']
                    # Convert COCO's bounding box coordinates to KITTI's
                    bbox = [bbox[0], bbox[1], bbox[2] +
                            bbox[0], bbox[3] + bbox[1]]
                    bbox = [str(b) for b in bbox]
                    catname = cat_idx[a['category_id']]
                    

                    # Format the line in the tag file
                    # Note: all white space will be removed from class names
                    # out_str = [catname.replace(" ", "") + ' ' + ' '.join(['0']*2) + join('-1') + ' ' + ' '.join([b for b in bbox]) + ' ' + ' '.join(['-1']*7) + '\n']
                    out_str = [f"{catname.replace(' ', '')} {'0 0 -1'} {' '.join(str(b) for b in bbox)} {'-1 -1 -1 -1 -1 -1 -1'}\n"]
                    print(out_str[0])
                    label_file.write(out_str[0])


if __name__ == '__main__':

    # # Establecer el modo "train" o "val"
    # mode = input('escriba un modo: ("train" o "val"): ')
    # name_dir = input('escriba el nombre del directorio principal:')

    # # Directorio de origen de imagenes
    # image_source_train = f'./{name_dir}/train'
    # image_source_val = f'./{name_dir}/valid'

    # # Directorio de destino de las labels
    # destination_labels_val = f'./{name_dir}/output/val/labels/'
    # destination_labels_train = f'./{name_dir}/output/train/labels/'

    # # Ruta hacia el archivo de anotación
    # source_directory_train = f'./{name_dir}/train'
    # source_directory_val = f'./{name_dir}/valid'

    # # Directorio de destino de imagenes
    # destination_images_train = '../output/train/images'  # no alterar
    # destination_images_val = '../output/val/images'  # no alterar

    # # Configuración de ruta del archivo de anotación
    # dataType = '_annotations.coco'

    # if mode == "train":
    #     image_source = image_source_train
    #     destination_images = destination_images_train
    #     destination_labels = destination_labels_train
    #     source_directory = source_directory_train
    #     annFile = f'{source_directory_train}/{dataType}.json'
    


    # if mode == "val":
    #     image_source = image_source_val
    #     destination_images = destination_images_val
    #     destination_labels = destination_labels_val
    #     source_directory = source_directory_val
    #     annFile = f'{source_directory_val}/{dataType}.json'

    # # Llama a la función para crear el directorio de imagens y moverlas a ese directorio
    # copys.crear_y_mover_directorio(image_source, destination_images)

    # # List of category names to include in KITTI tags

    catNms = ["person"]
    annFile = '/home/getter-lab/Vídeos/video_1/dataset_coco/labels.json'

    # # # Checks if a tag directory exists and if not, creates it
    # # # If it already exists, exit to avoid overwriting
    # if os.path.isdir(destination_labels):
    #     print('Labels folder already exists - exiting to prevent overwriting')
    # else:
    #     os.mkdir(destination_labels)
    coco2kitti(catNms, annFile)

        # annFile = f'{destination_images}/{dataType}.json'

        # # # Eliminar el archivo ".json" en el directorio de origen si existe
        # archivo_json = os.path.join(annFile)
        # if os.path.exists(archivo_json) and os.path.isfile(archivo_json):
        #     os.remove(archivo_json)
