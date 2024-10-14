# META Graph API Scraper

In the age of Artificial Intelligence and Big Data, social networks represent a valuable source of data, often regarded as a goldmine. This is a key reason why most social media APIs, particularly following the transformative launch of ChatGPT, have been restricted to use by specially authorized individuals.

This repository contains my Python implementation of a public data scraper for the META Graph API, specifically designed for the Facebook platform. It is limited to accessing data from public Facebook accounts only.

Additionally, I have conducted a basic sentiment analysis on the collected posts and provided a detailed explanation of the API's functionality in a Jupyter notebook.

------

## Dependencies

| Component | Version |
------------|----------
| Python    | `3.9`   |
| pip       | `24.0`  |

------

## Directory Structure

```bash
├── facebook_public_scraper
│   ├── main.py
│   ├── requirements.txt
│   ├── scraper.py
│   └── utils.py
├── Meta_Graph_API_tutorial
│   ├── Facebook Graph API tutorial.pdf
│   ├── META-sentiment-analysis.ipynb
│   └── README.md
└── README.md
```

------

## Usage

Clone the repo

```bash
git clone https://github.com/AndrewDarnall/META-Graph-API-Scraper.git
cd META-Graph-API-Scraper
```

Setup the dependencies

```bash
cd facebook_scraper
python -m pip install -r requirements.txt
```

Create a target file with a list of <i><b>public</b></i> facebook pages, usually you would call it `target.txt`

```bash
touch targets.txt
echo "NintendoAmerica" >> targets.txt
```

Run the scraper

```bash
python main.py targets.txt
```

Once finished, the scraper will have created in the current working directory `facebook_public_scraper` a directory, written in 
capital characters, of each scraped public page. <br>
Each directory contains images, text and raw .json of the scraped page's posts