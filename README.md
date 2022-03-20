# PythonImageTypeConversion
a python script that supports image conversion between jpeg and png

# Package Used
- PIL: Python imaging library (only supports to python 2.7)
    - Pillow, in replace of PIL, supports python 3 and above (same syntax as pillow)
- glob: unix style pathname pattern expansion

# Project Overview
- To convert PNG to JPEG
    - use im.convert('RGB') as JPEG doesn't store transparent colors
- To convert JPEG to PNG
    - use im.convert('RGBA') as PNG stores transparent colors ('A')
- Can set the quality label, the lower the quality, the smaller the image will be. Useful for smaller image at transmission
