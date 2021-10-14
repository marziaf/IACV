#!/usr/bin/python3


from os import listdir
from os.path import isfile, join

mypath = "exports"
files = listdir(mypath)

links = ""
for f in files:
    links += "<a href=\"{}\">{}</a> <br>".format(f, f.split(".")[0])

with open("index_template.html") as f:
    content = f.read()
    print(content)
    content=content.replace("LINKS_HERE", links)
    with open("index.html", "w") as index:
        index.write(content)

