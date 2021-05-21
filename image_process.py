#!/usr/bin/env python

import os
import sys
import PIL

if len(sys.argv) < 2:
    print("Please enter the image directory.")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Please enter only the image directory.")
    sys.exit(2)

for image in os.listdir(sys.argv[1]):
    print("test")
