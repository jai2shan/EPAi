
print('j2p is running')
from PIL import Image
import argparse
import os
def myj2p(path,newpath):
    for img in os.listdir(path):
        os.chdir(path)
        if '.jpg' in img:
            im = Image.open(img)
            os.chdir(newpath)
            im.save('png_'+img.split('.')[0]+'.png')
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
    myj2p(args.path,args.newpath)