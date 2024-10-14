import os
import json
from re import U
import requests


"""
    Helper object which saves the information regarding the scraped text from the facebook post

    @method __init__ : prepares the file
    @method log_text : logs the parsed text
    @method finish : releases the resources
"""
class TextLogger:

    fh = None

    def __init__(self, nam, ppath):
        va = ppath.strip() + "/" + nam.strip() + ".txt"
        self.fh = open(va,"w+")

    def log_text(self, text):
        self.fh.write(text)
        self.fh.write("\n")

    def finish(self):
        self.fh.close()

"""
    Helper object for the management of hyperlinks scraped by Facebook Public pages

    @method __init__ : creates and follows the hyperlink
    @method load_link : stores the scraped link
    @method terminate : releases the resources
"""
class LinkManager:

    f_name = None
    lh = None

    def __init__(self, f_name, ppath):
        self.f_name = f_name
        p = ppath.strip() + "/" + f_name.strip() + "_links.txt"
        self.lh = open(p,"w+")

    def load_link(self,link):
        self.lh.write(link['link'])
        self.lh.write("\n")

    def terminate(self):
        self.lh.close()

class JsonFormatter:

    scraped_file = ""
    count = 0
    payload = None
    ppath = None

    """
        Constructor for the JsonFormatter helper object

        @param fil : Scraped .json file
        @param ppath : Parent Path of scraped file
    """
    def __init__(self, fil, ppath):
        self.scraped_file = fil
        self.ppath = ppath
        new_path = ppath.strip() + "/JSON"
        os.mkdir(new_path)
        self.ppath = new_path

    """
        Method that loads the scraped .json file, formats it and saves it to an output directory
    """
    def load_json(self, payload):
        self.count += 1
        sava_name = self.ppath.strip() + "/" + self.scraped_file.strip() + str(self.count) + ".json"
        fh = open(save_name, "w+")
        obj = json.dumps(payload, indent=4, sort_keys=True, default=str)
        fh.write(obj)
        fh.write("\n")
        print("Finished Writing - {}".format(os.path.basename(self.scraped_file)))
        fh.close()

"""
    The class defines a helper method for the downloading of images from the scraped facebook posts
    of the scraped facebook (public) page
"""
class ImgDownloader:

    capture_name = ""
    num = 0
    url = None
    ppath = None

    """
        @param name: name of the 'captured' image
        @param ppath: the parent directoy path

    """
    def __init__(self, name, ppath):
        self.capture_name = name
        self.ppath = ppath
        new_path = ppath.strip() + "/IMG"
        self.ppath = new_path
        os.mkdir(new_path)

    """
        @param url : Image URL which points to Facebook's CDN which contains the specific image to be downloaded
    """
    def download(self, url):
        self.num += 1
        save_name = self.ppath.strip() + "/" + self.capture_name.strip() + str(self.num) + ".png"
        fh = open(save_name,"wb+")

        img_content = requests.get(url)
        if img_content.status_code:
            fh.write(img_content.content)
        print("captured - {}".format(os.path.basename(save_name)))
        fh.close()