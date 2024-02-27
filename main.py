import shutil
import os

desktop = "/root/"
destination = "/root/dealer-git/"

folders = [

"Photos",
"Documents",
"Music",
"Videos",
"Archives",
"Installers",
"Misc"

]

filetypes = [

".png .jpg .tif .jpeg .tiff",
".txt .doc .docx .ppt .pptx .xls .xlsx .rtf .pdf",
".mp3 .m4a .ogg .wav .flac .opus",
".mov .avi .mp4",
".zip r.gz ..bz2",
".exe .msi"

]

special = [

"Bluey",
"Mario",
"Linux"

]

for i in folders:
    if not os.path.exists(destination+i):
        os.mkdir(destination+i)
for i in special:
    if not os.path.exists(destination+i):
        os.mkdir(destination+i)

while True:

    for f in os.listdir(desktop):
        for d in special:
            if d.lower() in f.lower():
                try:
                    shutil.copy(desktop+f, destination+d+"/"+f)
                except:
                    0
        for d in range(len(filetypes)):
            if f[-4:].lower() in filetypes[d]:
                try:
                    shutil.copy(desktop+f, destination+folders[d]+"/"+f)
                except:
                    0
            if f[-5:].lower() in filetypes[d]:
                try:
                    shutil.copy(desktop+f, destination+folders[d]+"/"+f)
                except:
                    0
