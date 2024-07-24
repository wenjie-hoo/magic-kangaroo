---
title: ImageCompressionTool
date: 2024-07-23 14:34:58
cover: https://cdn.prod.website-files.com/632808d90ad3162f9c7ada64/64943240cfcffe7760bb7f19_Why%20Image%20Compression%20is%20Necessary.webp
categories: tech
tags: tech
---
Image lossless compression script for image backup

```python
import os
from PIL import Image

def imgToProgressive(path):
    if not path.split('.')[-1:][0] in ['png','JPG','jpg','jpeg']:  #if path isn't a image file,return
        return
    if os.path.isdir(path):
        return
    img = Image.open(path)
    exif = img.info['exif']
    destination = path.split('.')[:-1][0]+'_destination.'+path.split('.')[-1:][0]
    try:
        print(path.split('/')[-1:][0],'compressing image')
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True, exif=exif) 
        print(path.split('/')[-1:][0],'done')
    except IOError:
        PIL.ImageFile.MAXBLOCK = img.size[0] * img.size[1]
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True, exif=exif)
        print(path.split('/')[-1:][0],'done')
    print('renamed')
    os.remove(path)
    os.rename(destination,path)

for d,_,fl in os.walk(os.getcwd()):
    for f in fl:
        try:
            imgToProgressive(d+'/'+f)
        except:
            pass

```