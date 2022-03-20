# pip install Pillow
from PIL import Image  # Python Image Library - Image Processing

import glob #to identify files with particular extension

print(glob.glob("*.png")) #print list of files that are .png

# based on SO Answer: https://stackoverflow.com/a/43258974/5086335
for file in glob.glob("*.png"):
    im = Image.open(file)
    #we dont use rgba here since a stands for transparency, which is what jpg can't hold
    #however if transforming from jpg to png, we can use rbga
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95) #the lower the quality, the smaller the size (more suitable for upload)


'''
import os
for file in glob.glob("*.jpg"):
    os.remove(file)
'''
