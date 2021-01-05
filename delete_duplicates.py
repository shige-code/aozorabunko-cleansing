import re

f = open("all_wakati.txt","r")
read_text = f.readlines()
read_text = [line.strip() for line in read_text]
read_text = set(read_text)

s = str(read_text)

result = re.sub(r"['}{ ]","",s)
result2 = result.replace(",","\n")

print(result2)

