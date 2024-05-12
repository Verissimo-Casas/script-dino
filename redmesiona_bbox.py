import os

# Directory paths
original_dir = '/home/getter-lab/Vídeos/video_1/labels'
new_dir = '/home/getter-lab/Vídeos/video_1/labels'

# Create the new directory if it doesn't exist
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# Function to expand bounding boxes
def expand_bbox(bbox, expansion_factor=0.14, image_width=1920, image_height=1080):
    """
    Expands a bounding box by a given factor without altering its original centroid,
    and ensures it does not exceed the image boundaries.
    
    Parameters:
    - bbox (tuple): The original bounding box coordinates in the format (x1, y1, x2, y2).
    - expansion_factor (float): The factor by which to expand the bounding box. Default is 0.12.
    - image_width (int): The width of the image. Default is 1920.
    - image_height (int): The height of the image. Default is 1080.
    
    Returns:
    - tuple: The expanded bounding box coordinates in the format (x1, y1, x2, y2).
    """
    x1, y1, x2, y2 = bbox
    width = x2 - x1
    height = y2 - y1
    centroid_x = (x1 + x2) / 2
    centroid_y = (y1 + y2) / 2
    
    # Calculate the new width and height after expansion
    new_width = width * (1 + expansion_factor)
    new_height = height * (1 + expansion_factor)
    
    # Calculate the expansion needed to maintain the centroid
    expansion_x = (new_width - width) / 2
    expansion_y = (new_height - height) / 2
    
    # Expand the bbox while maintaining the centroid
    expanded_x1 = centroid_x - new_width / 2
    expanded_y1 = centroid_y - new_height / 2
    expanded_x2 = centroid_x + new_width / 2
    expanded_y2 = centroid_y + new_height / 2
    
    # Ensure the expanded bbox does not exceed the image boundaries
    expanded_x1 = max(0, expanded_x1) # Ensure x1 is not less than 0
    expanded_y1 = max(0, expanded_y1) # Ensure y1 is not less than 0
    expanded_x2 = min(image_width, expanded_x2) # Ensure x2 does not exceed image width
    expanded_y2 = min(image_height, expanded_y2) # Ensure y2 does not exceed image height
    
    # Adjust the expansion if it exceeds the image boundaries
    if expanded_x1 < 0 or expanded_y1 < 0 or expanded_x2 > image_width or expanded_y2 > image_height:
        # Calculate the maximum expansion that can be applied without exceeding the image boundaries
        max_expansion_x = min(centroid_x, image_width - centroid_x)
        max_expansion_y = min(centroid_y, image_height - centroid_y)
        
        # Apply the maximum possible expansion
        expanded_x1 = centroid_x - max_expansion_x
        expanded_y1 = centroid_y - max_expansion_y
        expanded_x2 = centroid_x + max_expansion_x
        expanded_y2 = centroid_y + max_expansion_y
    
    return (expanded_x1, expanded_y1, expanded_x2, expanded_y2)


# Process each file in the original directory
for filename in os.listdir(original_dir):
    if filename.endswith(".txt"): # Assuming the labels are in .txt files
        original_file_path = os.path.join(original_dir, filename)
        new_file_path = os.path.join(new_dir, filename)
        
        # Read the labels from the original file
        with open(original_file_path, 'r') as file:
            lines = file.readlines()
        
        # Process each line to expand the bounding boxes
        expanded_labels = []
        for line in lines:
            parts = line.strip().split()
            class_label = parts[0]
            # Assuming the missing values are at positions [0:4] and should be 0
            missing_values = "0 0 -1"
            bbox = list(map(float, parts[4:8])) # Assuming bbox is in positions 4 to 7
            expanded_bbox = expand_bbox(bbox)
            expanded_line = f"{class_label} {missing_values} {' '.join(map(str, expanded_bbox))} {' '.join(parts[8:])}\n"
            expanded_labels.append(expanded_line)
        
        # Write the expanded labels to a new file in the new directory
        with open(new_file_path, 'w') as file:
            file.writelines(expanded_labels)
