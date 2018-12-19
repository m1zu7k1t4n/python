from xml.dom import minidom
import os
import pathlib
import shutil
import re
import sys
FileType = sys.argv[1]
TargetPath = "D:\\CACHE"
p = pathlib.Path(TargetPath)
# 最下層ディレクトリを列挙
Deepest = list()
def searchOPF(directory):
    for path in directory.iterdir():
        if not (x for x in path.iterdir() if x.is_dir()):
            Deepest.append(path)
        else:
            searchOPF(path)
searchOPF(p)
# 各最下層ディレクトリの.opfを取得
if not os.path.isdir(str(p) + "\\kindle"):
    os.mkdir(str(p) + "\\kindle")
for path in Deepest:
    try:
        opf = list(path.glob('*.opf'))[0]
        pdf = list(path.glob('*.' + FileType))[0]
    except:
        continue
    xdoc = minidom.parse(str(opf))
    title_element = xdoc.getElementsByTagName("dc:title")[0]
    replace_name = title_element.childNodes[0].data
    replace_name = re.sub(r'[\/:*?"<>|]+','_',replace_name)
    replace_name = str(path) + "\\" + replace_name + "." + FileType
    os.rename(pdf, replace_name)
    shutil.move(replace_name, str(p) + "\\kindle")
