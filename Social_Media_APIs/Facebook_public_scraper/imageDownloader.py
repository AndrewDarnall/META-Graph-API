# Image downloader component for my scraper project
from re import U
import requests
import os

class ImgDownloader:

    captureName = ""
    num = 0
    url = None
    ppath = None

    def __init__(self, name,ppath):
        self.captureName = name
        self.ppath = ppath
        newPath = ppath.strip() + "/IMG"
        self.ppath = newPath
        os.mkdir(newPath)


    def download(self,url):
        self.num += 1
        saveName = self.ppath.strip() + "/" + self.captureName.strip() + str(self.num) + ".png"
        fh = open(saveName,"wb+")

        img_content = requests.get(url)
        if img_content.status_code:
            fh.write(img_content.content)
        print("captured - {}".format(os.path.basename(saveName)))
        fh.close()
# End of component class