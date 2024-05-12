#abrir imagem com opencv
import cv2

#carregar imagem
img = cv2.imread('/home/getter-lab/Vídeos/VideosOriginal/video10/dino/video10_0231.jpg')

#mostrar imagem
cv2.imshow('image', img)
cv2.waitKey(0)

#fechar janela

cv2.destroyAllWindows()


