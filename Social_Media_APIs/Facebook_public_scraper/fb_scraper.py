# The Facebook public scraper ~ By TheComputerScientist (Drew)

# https://github.com/kevinzg/facebook-scraper
from facebook_scraper import get_posts
import jsonDowmloader
import imageDownloader
import textLogger
import linkManager
import os
import sys
import re

class Scraper:

    fileName = ""
    txt = None
    img = None
    jsn = None
    lnk = None
    num = None
    cwd = None
    path = None

    def __init__(self,fName):
        self.fileName = fName
        self.num = 0
        self.cwd = os.getcwd()
        upr = self.fileName.upper()
        self.path = os.path.join(self.cwd,upr.strip())
        os.mkdir(self.path)
        self.txt = textLogger.TextLogger(fName,self.path)
        self.img = imageDownloader.ImgDownloader(fName,self.path)
        self.jsn = jsonDowmloader.JsonFormatter(fName,self.path)
        self.lnk = linkManager.LinkManager(fName,self.path)

    def scrape(self):

        for post in get_posts(self.fileName, pages=20, options={'progress':True}):
            self.num += 1
            self.txt.logText(post['text'][:100])
            self.jsn.loadJson(post)

            if post['image'] != None:
                self.img.download(post['image'])
            elif post['image_lowquality'] != None:
                self.img.download(post['image_lowquality'])
            elif post['images'] != None:
                self.img.download(post['images'])
            elif post['images_lowquality'] != None:
                self.img.download(post['images_lowquality'])

            if post['links'] != None:
                self.lnk.loadLink(post['links'][0])

        print("Finished scraping page:\t({})".format(self.fileName))
        self.txt.finish()
        self.lnk.terminate()



class ScraperManager:

    file = None

    def __init__(self,file):
        self.file = file

    def startScrape(self):
        fh = open(self.file,"r")
        for line in fh:
            scraper = Scraper(line)
            scraper.scrape()
            


# Main
if len(sys.argv) != 2:
    print("Usage:\t<{}>\t<input-file>".format(sys.argv[0]))
    sys.exit(1)

x = re.search("\.txt", sys.argv[1])

if x:
    print("Scraping from input file: [{}]".format(sys.argv[1]))
else:
    print("Must read from a TEXT file!")

print("Starting Scraper")
scr = ScraperManager(sys.argv[1])
scr.startScrape()