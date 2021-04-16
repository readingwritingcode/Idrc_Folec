#!/usr/bin/env python
# this module translate paragraphs

import sys
from googletrans import Translator
#print(googletrans.LANGUAGES)

def translator(paragraph):
    '''this is a module for use in other scripts'''

    tr = Translator(service_urls=[
      'translate.google.com.ar',
      'translate.google.com.ch',
      'translate.google.com.co',
      'translate.google.com.br',
      'translate.google.com.bo',
      'translate.google.com.pa'
    ])

    pt = tr.translate(paragraph,dest='en')

    return pt.text

if __name__ == "__main__":

    prgh = sys.argv[1]
    prgh_tr = translator(prgh)
    print(prgh)