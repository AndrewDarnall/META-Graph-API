# Facebook Story Link manager component
import os

class LinkManager:

    fName = None
    lh = None

    def __init__(self,fName,ppath):
        self.fName = fName
        p = ppath.strip() + "/" + fName.strip() + "_links.txt"
        self.lh = open(p,"w+")

    def loadLink(self,link):
        self.lh.write(link['link'])
        self.lh.write("\n")

    def terminate(self):
        self.lh.close()