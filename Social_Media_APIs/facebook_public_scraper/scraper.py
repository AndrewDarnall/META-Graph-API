from facebook_scraper import get_posts
from utils import TextLogger
from utils import LinkManager
from utils import JsonFormatter
from utils import ImgDownloader
import os

"""
    Scraper driver object

    @method scrape : a wrapper which uses the methods defined in the utility.py module
"""
class Scraper:

    file_name = ""
    txt = None
    img = None
    jsn = None
    lnk = None
    num = None
    cwd = None
    path = None

    def __init__(self, f_name):
        self.file_name = f_name
        self.num = 0
        self.cwd = os.getcwd()
        upr = self.file_name.upper()
        self.path = os.path.join(self.cwd,upr.strip())
        os.mkdir(self.path)
        self.txt = TextLogger(f_name, self.path)
        self.img = ImgDownloader(f_name, self.path)
        self.jsn = JsonFormatter(f_name, self.path)
        self.lnk = LinkManager(f_name, self.path)

    def scrape(self):

        for post in get_posts(self.file_name, pages=20, options={'progress':True}):
            self.num += 1
            if post['text'] != None:
                self.txt.log_text(post['text'][:100])
            self.jsn.load_json(post)

            if post['image'] != None and len(post['image']) != 0 and post['image'][0] != None:
                self.img.download(post['image'])
            elif post['image_lowquality'] != None and len(post['image_lowquality']) != 0 and post['image_lowquality'][0] != None:
                self.img.download(post['image_lowquality'])
            elif post['images'] != None and len(post['images']) != 0 and post['images'][0] != None:
                self.img.download(post['images'])
            elif post['images_lowquality'] != None and len(post['images_lowquality']) != 0 and post['images_lowquality'][0] != None:
                self.img.download(post['images_lowquality'])

            if post['links'] != None:
                self.lnk.load_link(post['links'][0])

        print("Finished scraping page:\t({})".format(self.file_name))
        self.txt.finish()
        self.lnk.terminate()


"""
    Facede Object for the Scraper

    @method start_scraper : opens the file of public pages to scrape and scrapes each entry
"""
class ScraperManager:

    file = None

    def __init__(self,file):
        self.file = file

    def start_scraper(self):
        fh = open(self.file, "r")
        for line in fh:
            scraper = Scraper(line)
            scraper.scrape()