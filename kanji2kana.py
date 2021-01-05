from pykakasi import kakasi
import re

f = open('kanji_goi.txt')
text = f.readline()

kakasi = kakasi()
# モードの設定：J(Kanji) to K(Katakana)
kakasi.setMode('J', 'K')
conv = kakasi.getConverter()

while text:
    text = re.sub(r"[a-xA-Z0-9_]","",text)
    text = conv.do(text)
    text = text.rstrip("\n")
    print(text)
    text = f.readline()
f.close