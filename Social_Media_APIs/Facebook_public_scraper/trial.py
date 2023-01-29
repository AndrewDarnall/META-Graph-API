# Trial scrpit to check if the public page is scrapable
from facebook_scraper import get_posts
import os

pageName = input("Enter PUBLIC page name: ")

for post in get_posts(pageName, pages=3, options={"progress":True}):
    print(post['text'][:50])
    os._exit(1)


print("[{}] scrape finished".format(pageName))