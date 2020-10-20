
print('p2j is running')
from PIL import Image
import argparse
import os
def myp2j(path,newpath):
    for img in os.listdir(path):
        os.chdir(path)
        if '.png' in img:
            im = Image.open(img)
            rgb_im = im.convert('RGB')
            os.chdir(newpath)
            rgb_im.save('jpg_'+img.split('.')[0]+'.jpg')
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-path',
                        type = str,
                        help = 'This is running in main')
    parser.add_argument('-newpath',
                        type = str,
                        help = 'This is running in main')
    args = parser.parse_args()
    myp2j(args.path,args.newpath)