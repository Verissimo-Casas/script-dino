import cv2

# Load the image

image = cv2.imread('/home/getter-lab/Vídeos/new_dataset/coco_dataset/data/image_0428.png')

dic_rectangles = {
    'rec1': (785.0415229797363, 249.05173301696777, 914.5474433898926, 516.0418438911438),
    'rec2': (0.28127431869506836, 444.00673270225525, 123.13537359237671, 686.6755270957947),
    # 'rec3': (340.8659076690674, 539.5435309410095, 601.1374282836914, 864.5895409584045)
}





# Assuming the image dimensions are known
image_width = 1920
image_height = 1080

expanded_rectangles = {}

for name, bbox in dic_rectangles.items():
    x1, y1, x2, y2 = bbox
    width = x2 - x1
    height = y2 - y1
    expansion_x = width * 0.12 / 2
    expansion_y = height * 0.12 / 2
    
    # Expand the bbox
    expanded_x1 = x1 - expansion_x
    expanded_y1 = y1 - expansion_y
    expanded_x2 = x2 + expansion_x
    expanded_y2 = y2 + expansion_y
    
    # Ensure the expanded bbox does not exceed the image boundaries
    expanded_x1 = max(0, expanded_x1)
    expanded_y1 = max(0, expanded_y1)
    expanded_x2 = min(image_width, expanded_x2)
    expanded_y2 = min(image_height, expanded_y2)
    
    expanded_rectangles[name] = (expanded_x1, expanded_y1, expanded_x2, expanded_y2)
    image_expanded = cv2.rectangle(image, (int(expanded_x1), int(expanded_y1)), (int(expanded_x2), int(expanded_y2)), (0, 0, 255), 2)



# Draw the rectangles
for rectangle in dic_rectangles.values():
    x1, y1, x2, y2 = rectangle
    # image = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

# Display the image
# cv2.imshow('image', image)
cv2.imshow('image_expanded', image_expanded)
cv2.waitKey(0)