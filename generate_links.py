#!/usr/bin/python3


from os import listdir
from os.path import isfile, join

mypath = "exports"
files = sorted(listdir(mypath))

links = ""
for f in files:
    links += "<a href=\"{}\">{}</a> <br>".format(mypath + "/" + f, f.split(".")[0])

with open("index_template.html") as f:
    content = f.read()
    content=content.replace("LINKS_HERE", links)
    print("Replacing index with real links")
    with open("index.html", "w") as index:
        index.write(content)

