import MeCab
import re

tagger = MeCab.Tagger("-Owakati")

f = open("all.txt","r")
read_text = f.readlines()
f.close()

for text in read_text:
    result = re.sub(r"[a-xA-Z0-9_]","",text)
    result = tagger.parse(text)
    
    with open("read_test_result.txt", mode="a") as write_file:
        result = result.replace(" ","\n")
        print(result)
