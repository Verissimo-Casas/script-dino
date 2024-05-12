import os
import shutil
from pycocotools.coco import COCO

def crear_y_mover_directorio(origen, nombre_destino):
    destino = os.path.join(origen, nombre_destino)
    if not os.path.exists(destino):
        os.makedirs(destino)
    return destino 

def coco2kitti(catNms, annFile, origen, nombre_destino):
    coco = COCO(annFile)
    cats = coco.loadCats(coco.getCatIds())
    
    cat_idx = {c['id']: c['name'] for c in cats}
    
    destino_labels = crear_y_mover_directorio(origen, nombre_destino)
    
    for img_id in coco.imgs:
        catIds = coco.getCatIds(catNms=catNms)
        annIds = coco.getAnnIds(imgIds=[img_id], catIds=catIds)
        
        if annIds:
            img_fname = coco.imgs[img_id]['file_name']
            with open(os.path.join(destino_labels, img_fname[:-4] + '.txt'), 'w') as label_file:
                anns = coco.loadAnns(annIds)
                for a in anns:
                    bbox = [a['bbox'][0], a['bbox'][1], a['bbox'][2] + a['bbox'][0], a['bbox'][3] + a['bbox'][1]]
                    catname = cat_idx[a['category_id']]
                    out_str = f"{catname.replace(' ', '')} {'0 0 -1'} {' '.join(str(b) for b in bbox)} {'-1 -1 -1 -1 -1 -1 -1 1.0'}\n"
                    label_file.write(out_str)

# Exemplo de uso
catNms = ['person']
annFile = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/labels.json'
origen = '/home/getter-lab/Vídeos/video_1/luva_nitrilica/label_2'
nombre_destino = 'labels_2'

coco2kitti(catNms, annFile, origen, nombre_destino)
