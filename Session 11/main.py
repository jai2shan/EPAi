import argparse
import j2p
import p2j
import os

def listfiles(path):
    print(os.listdir(path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-path',
                        type = str,
                        help = 'This is running in main')
    parser.add_argument('-newpath',
                        type = str,
                        help = 'This is running in main')
    parser.add_argument('-j2p',
                        type = bool,
                        help = 'This is running in main')
    parser.add_argument('-p2j',
                        type = bool,
                        help = 'This is running in main')
    args = parser.parse_args()
    if args.j2p:
        j2p.myj2p(args.path, args.newpath)
    if args.p2j:
        p2j.myp2j(args.path, args.newpath)

