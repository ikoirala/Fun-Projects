import os
from PIL import Image

# Crops the image and saves it as "new_filename"

x = [i[2] for i in os.walk('.')]
y = []
for t in x:
    for f in t:
        if f == '.DS_Store' or f == 'crop_photo.py':
            continue
        y.append(f)

y.sort()
# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)
crop_area = (3356, 315, 6625, 3704)

# Loops through the "crop_areas" list and crops the image based on the coordinates in the list
for image_name in y:
    print(image_name)
    img = Image.open(image_name)
    filename = os.path.splitext(image_name)[0]
    ext = os.path.splitext(image_name)[1]
    new_filename = filename + '_cropped' + ext
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)