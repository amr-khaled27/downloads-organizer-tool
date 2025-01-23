import os
import shutil
from pathlib import Path


target = str(Path.home() / "Downloads") + "\\"
files = os.listdir(target)

imageExtentions = ["png", "jpg", "jpeg", "svg", "PNG"]
VideoExtentions = ["mp4", "mov"]
audioExtentions = ["mp3", "wav"]
archiveExtentions = ["rar", "zip", "7z"]


def createAndMove(file, dir):
    if not os.path.exists(target + dir):
        os.mkdir(target + dir)
        shutil.move(target + file, target + dir + file)
    else:
        shutil.move(target + file, target + dir + file)


for file in files:
    filename, extention = os.path.splitext(file)
    extention = extention[1:]
    if os.path.isfile(target + file):
        if extention in imageExtentions:
            createAndMove(file, "Downloaded Photos\\")
        elif extention in VideoExtentions:
            createAndMove(file, "Downloaded Videos\\")
        elif extention in audioExtentions:
            createAndMove(file, "Downloaded Audios\\")
        elif extention in archiveExtentions:
            createAndMove(file, "Downloaded Archives\\")
        elif extention == "pdf":
            createAndMove(file, "Downloaded Pdf\\")
        elif extention.lower() == "tmp" or extention.lower() == "crdownload" or extention.lower() == "fdmdownload":
            pass
        else:
            createAndMove(file, "Downloaded " + extention + "\\")
