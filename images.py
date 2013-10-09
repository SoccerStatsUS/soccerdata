import os
import shutil


# For converting MLS press box image names.

def rename_mls_image(s):
    m = s.split('- ')[0]
    last, first = m.split(',')
    return "%s-%s.jpg" % (first.lower(), last.lower())


def convert_folder(p):
    for fn in os.listdir(p):
        fp = os.path.join(p, fn)
        try:
            nfn = rename_mls_image(fn)
            nfp = os.path.join(p, nfn)
            shutil.move(fp, nfp)
        except:
            os.remove(fp)



        



