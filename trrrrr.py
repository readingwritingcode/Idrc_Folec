from googletrans import Translator

paragraph = "hola"

tr = Translator()

pt = tr.translate(paragraph,src = 'es',dest='en')

print(pt.text)