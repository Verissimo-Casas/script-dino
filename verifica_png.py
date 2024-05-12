import os
import re

# Define the directories
image_dir = '/home/getter-lab/Vídeos/video_3/images/'
label_dir = '/home/getter-lab/Vídeos/video_3/labels/'

# Get a list of all .png files in the image directory
image_files = [f for f in os.listdir(image_dir) if re.match(r'^.*\.png$', f)]

# Get a list of all .txt files in the label directory
label_files = [f for f in os.listdir(label_dir) if re.match(r'^.*\.txt$', f)]

# Extract the base names (without extensions) from these file names
image_base_names = [os.path.splitext(f)[0] for f in image_files]
label_base_names = [os.path.splitext(f)[0] for f in label_files]

# Find the .txt files that do not have a corresponding .png file
missing_images = set(label_base_names) - set(image_base_names)

# Delete the .txt files that do not have a corresponding .png file
for missing_image in missing_images:
    os.remove(os.path.join(label_dir, missing_image + '.txt'))

print(f"Deleted {len(missing_images)} .txt files without corresponding .png files.")
