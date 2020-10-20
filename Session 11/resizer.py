from PIL import Image
img = r'C:\Users\jayasans4085\OneDrive - ARCADIS\Desktop\results\Source\im_01.jpg'

def resizer(img,res_p=False,res_w=False,res_h=False):
    im = Image.open(img)
    width,height = im_size
    if res_p!=False:
        new_width, new_height = width * res_p, height * res_p
        im = im.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        im.save('res_p_'+img)
        print(1)

    elif res_w != False:
        percent = res_w/width
        new_width, new_height = res_w, height*percent
        im = im.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        im.save('res_w_'+img)
        print(2)

    elif res_h!= False:
        percent = res_h / height
        new_width, new_height = width * percent , res_h
        im = im.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        im.save('res_h_'+img)
        print(3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-path',
                        type = str,
                        help = 'This is running in main')
    parser.add_argument('-newpath',
                        type = str,
                        help = 'This is running in main')
    args = parser.parse_args()
    for img in os.listdir(args.path):
        os.chdir()
    myp2j(args.path,args.newpath)
resizer(img,res_p=False,res_w=False,res_h=False)