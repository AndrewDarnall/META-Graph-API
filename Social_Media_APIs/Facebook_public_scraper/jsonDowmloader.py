# JSON file formatter component
import json
import os

class JsonFormatter:

    scrapedFile = ""
    count = 0
    payload = None
    ppath = None

    def __init__(self,fil,ppath):
        self.scrapedFile = fil
        self.ppath = ppath
        newPath = ppath.strip() + "/JSON"
        os.mkdir(newPath)
        self.ppath = newPath

    def loadJson(self,payload):
        self.count += 1
        saveName = self.ppath.strip() + "/" + self.scrapedFile.strip() + str(self.count) + ".json"
        fh = open(saveName,"w+")
        obj = json.dumps(payload, indent=4, sort_keys=True, default=str)
        fh.write(obj)
        fh.write("\n")
        print("Finished Writing - {}".format(os.path.basename(self.scrapedFile)))
        fh.close()
# End of JSON format component