# Disclaimer

This program was written purely for accademic purposes, I do not endorse stealing
data from Social Media platforms without their explicit consent (i.e. API access).

# Dependencies

- requests

# Final Notes of the scraper

A more ambitious project would be to scrape any page I saught to scrape
this however can only be done by extracting ALL of the text and links
present in the soup version of the html document and such process would
undoubtedly introduce a certain ammount of noise in the data, plus
it would attract some attention to the scraper's account since the program
would need to 'fool' Meta by sending an appropriate payload with username and
password

# Usage

- To run -> python3 fb_scraper.py 'targets_file.txt'

The scraper needs to have a text file as input with the names of all of the public pages that you intend to scrape, however I included a trial.py script which
tests wether the scraper will actually scrape information from the page or not,
this is done to avoid wasting the allocating of directories (and having to delete them afterwards).
The limitations of the scraper are mentioned in the official GitHub page.
The trial.py simply prompts for the name of the target page and if it is scrapable
you will see one line scraped from the page, otherwise it will terminate with a 
message that claims that the page was scraped nut nothing else will have been
printed to stdout.

Upon succesful scraping of the public page, you will find within the work. dir.
where the program was summoned a directory with the upper case name of the scraped
page, two sub directories, IMG and JSON and an additional two text files, one for
the comments and the other with the story links if present, the story links can be 
used to extract the comments by using an additional program that sends requests on 
the user's behalf (using the user's password and username -> secrets.py) to retreive
likes and comments.

By tweaking the pages= parameters in the get_posts() function, the user can increase
decrese the data intake.