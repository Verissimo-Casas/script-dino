import cv2
import os

def crop_images(image_folder, label_folder, output_folder):
    # Iterate over the files in the image folder
    for image_file in os.listdir(image_folder):
        if image_file.endswith('.png') or image_file.endswith('.jpg'):  # Verify if it's an image file
            image_path = os.path.join(image_folder, image_file)
            label_file = os.path.splitext(image_file)[0] + '.txt'  # Corresponding label file name
            label_path = os.path.join(label_folder, label_file)
            
            # Read the image
            image = cv2.imread(image_path)
            
            # Check if the label file exists
            if os.path.exists(label_path):
                # Read the coordinates from the label file
                with open(label_path, 'r') as file:
                    lines = file.readlines()
                
                # Process each line and crop the image
                for i, line in enumerate(lines, start=1):
                    parts = line.strip().split(' ')
                    
                    # Extract coordinates
                    x1, y1, x2, y2 = map(float, parts[4:8])
                    
                    # Convert coordinates to integers
                    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                    
                    # Crop the image
                    cropped_image = image[y1:y2, x1:x2]
                    
                    # Save the cropped image with the desired file name format
                    output_file = f'cropped_{os.path.splitext(image_file)[0]}_object{i}.png'
                    output_path = os.path.join(output_folder, output_file)
                    cv2.imwrite(output_path, cropped_image)
                    
                    print(f'Cropped image {output_file} saved.')
            else:
                print(f'Label file not found for image: {image_file}')



if __name__ == '__main__':
    image_folder = '/home/getter-lab/Vídeos/video_1/images/'
    label_folder = '/home/getter-lab/Vídeos/video_1/labels/'
    output_folder = '/home/getter-lab/Vídeos/video_1/cropped_images/'
    
    crop_images(image_folder, label_folder, output_folder)
    print('Image cropping completed.')