# Facebook post text logger

class TextLogger:

    fh = None

    def __init__(self,nam,ppath):
        va = ppath.strip() + "/" + nam.strip() + ".txt"
        self.fh = open(va,"w+")

    def logText(self,text):
        self.fh.write(text)
        self.fh.write("\n")

    def finish(self):
        self.fh.close()