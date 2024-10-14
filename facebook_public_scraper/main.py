from scraper import ScraperManager
import sys
import re

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
scr.start_scraper()