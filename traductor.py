#!/usr/bin/env python
# This is a program for translate pdf documents
# input pdfs
# output text in txt format
# author dave

import sys
import time
import extractor
import translator

from httpcore._exceptions import ConnectError

def traductor(path_to_pdf):

    lop = extractor.extractor(path_to_pdf)[1]

    idx = 0
    str_var = ''

    for p in lop:

        #print(p)

        fails = 0
        vc = True

        while vc:
            try:

                pt = translator.translator(p)
                print(pt)

                if pt is not None:

                    str_var += pt + '\n'
                    vc = False

            except ConnectError as e:

                if fails <3:

                    time.sleep(5)
                    print('sleeping a moment')

                else:

                    vc = False
                    str_var += '%s not posible to trans' % idx
        idx += 1
        time.sleep(1)

    return str_var

if __name__ == '__main__':

    path = sys.argv[1]
    pdf_tr = traductor(path)
    print(pdf_tr)