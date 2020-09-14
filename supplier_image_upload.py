#!/usr/bin/env python3

import requests
import os

url = 'http://localhost/upload/'
dist_dir = './supplier-data/images/'

for image in os.listdir(dist_dir):
    if 'jpeg' in image:
        with open(dist_dir + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

