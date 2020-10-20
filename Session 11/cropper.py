from PIL import Image
import os
os.chdir(r'C:\Users\jayasans4085\OneDrive - ARCADIS\Desktop\results\Source')


def crp_px(path,crop_w,crop_h = 0):

    for img in [_ for _ in os.listdir(path) if '.' in _]:
        os.chdir(path)
        im = Image.open(r"im_01.png")
        width, height = im.size

        if crop_h==0:
            crop_h = crop_w

        if (crop_w>im.size[0]) & (crop_h>im.size[1]):
            print("Cropping parameter is bigger than one of the dimensions of the image")
        else:
            center_w,center_h = im.size[0]/2,im.size[1]/2
            left = center_w-crop_w/2
            right = center_w+crop_w/2
            top = center_h-crop_h/2
            bottom = center_h+crop_h/2
            im = im.crop((left,top,right,bottom))
            im.save("Cropped "+img)