#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import PIL
import os

dist_dir = './supplier-data/images/'

for image in os.listdir(dist_dir):
    if 'tiff' in image:
        image_name = image.split('.')[0]
        image_path = os.path.join(dist_dir, image)
        im = Image.open(image_path)
        print (image_path, ' => Done')
        if im.mode != 'RGB':
            im = im.convert('RGB')
        new_image_path = os.path.join(dist_dir, image_name)
        im.resize((600, 400)).save('{}.jpeg'.format(new_image_path),'JPEG')

