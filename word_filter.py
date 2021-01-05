import glob
import MeCab
import re
import codecs

txt = "./all_clean_shift_jis.txt"
f = open(txt)
data = f.read()

tokenizer = MeCab.Tagger("mecabrc")
tokenizer.parse("")
node = tokenizer.parseToNode(data)
keywords = []
while node:
    if node.feature.split(",")[0] == u"名詞":
        print(node.surface)
    elif node.feature.split(",")[0] == u"形容詞":
        print(node.feature.split(",")[6])
    elif node.feature.split(",")[0] == u"動詞":
        print(node.feature.split(",")[6])
    node = node.next
print(node)