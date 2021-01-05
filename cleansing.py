import glob
import re

files = glob.glob("./cards/*/files/*.html")

for html_file in files:
    f = open(html_file, 'r', encoding='Shift-JIS')
    data = f.read()
    p = re.compile(r"<[^>]*?>")
    txt = p.sub("", data)
    clean_txt = re.sub(r"[,.!?: ;'　？\t！\n]", "", txt)
    print(clean_txt)