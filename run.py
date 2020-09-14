#! /usr/bin/env python3

import os
import requests

entry = {
	"name": "",
	"weight": 0,
	"description": "",
	"image_name": ""
	}

dist_dir = './supplier-data/images/'
url = 'http://localhost/upload/'

for image in os.listdir(dist_dir):
    if 'jpeg' in image:
        image_name = image.split('.')[0]
	desc_path = './supplier-data/descriptions/' + image_name + ".txt"
	with open(desc_path, 'r') as file:
		for i in ["name", "weight", "description"]:
			entry[i] = file.readline()
	entry["image_description"] = dist_dir + image
	r = requests.post(url, data=entry, files={'file': image})

