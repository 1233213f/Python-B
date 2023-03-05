from PIL import Image
import os
folderPath = "https://wenku.baidu.com/view/7c004a4dfbb069dc5022aaea998fcc22bdd14374.html?fr=sezrch-1-wk_sea-income3"
filename = "test"
files = os.listdir(folderPath)
jpgFiles = []
sources = []
for file in files:
    if 'jpg' in file:
        jpgFiles.append(file)
tep = []
for i in jpgFiles:
    ex = i.split('.')
    tep.append(int(ex[0]))
tep.sort()
jpgFiles=[folderPath +'/'+ str(i) + '.jpg' for i in tep]
output = Image.open(jpgFiles[0])
jpgFiles.pop(0)
for file in jpgFiles:
   img = Image.open(file)
   img = img.convert("P")
   sources.append(img)
output.save(f"./{filename}.pdf","PDF",save_all=True,append_images=sources)