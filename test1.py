import json

with open('/home/getter-lab/Vídeos/video_7/person-coco/labels.json', 'r') as file:
    data = json.load(file)

areas = {
    "area_1": (0.0, 0.0, 614.2, 335.1),
    "area_2": (615.14, 0.0, 1035.16, 194.9),
    "area_3": (1661.3, 0.05, 258.7, 512.95)
}

annotations = data['annotations']

def point_in_rect(point, rect):
    x1, y1, w, h = rect
    x2, y2 = x1 + w, y1 + h
    x, y = point
    if (x1 < x and x < x2) and (y1 < y and y < y2):
        return True
    return False

# Modified filtering logic to use centroids
filtered_annotations = [
    annotation for annotation in annotations
    if not any(
        point_in_rect((annotation["bbox"][0] + annotation["bbox"][2]/2, annotation["bbox"][1] + annotation["bbox"][3]/2), area_rect)
        for area_name, area_rect in areas.items()
    )
]

# Convert the filtered list of dictionaries into a JSON string
json_data = json.dumps(filtered_annotations, indent=2)

# Save the JSON string to a file
with open('filtered_annotations.json', 'w') as json_file:
    json_file.write(json_data)
