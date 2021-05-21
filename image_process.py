#!/usr/bin/env python

import os
import sys
from PIL import Image

if len(sys.argv) < 2:
    print("Please enter the image directory.")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Please enter only the image directory.")
    sys.exit(2)

root = sys.argv[1]
os.mkdir(os.path.join(root,"jpeg"))
for f in os.listdir(root):
    if not f.startswith(".") and os.path.isfile(os.path.join(root,f)):
        print(os.path.join(root,f))
        with Image.open(os.path.join(root,f)) as image:
            theta = 270
            image.convert("RGB").rotate(theta).resize((128,128)).save(fp=os.path.join(root,"jpeg",f),format="JPEG")
