import os

x = [i[2] for i in os.walk('.')]
y = []
for t in x:
    for f in t:
        if f == '.DS_Store' or f == 'index.html' or f == 'list_of_image.py':
            continue
        y.append(f)
y.sort()

# Loops through the list
for image_name in y:
    print('            <p><img src="imgTh/' + image_name + '" alt="" /></p>')