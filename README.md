# Quote Scraper
This web scraping project scrapes quotes from BrainQuote.com. The user can specify a quote category and the number of quotes they'd like to fetch. The scraped data is written to text files in the src/Quotes directory.

### Setup:
1. Clone this repo and change into the drivers directory
```
git clone https://github.com/Tymotex/Quote-scraping.git
```
2. Find out your chrome version. Type in the URL bar: chrome://version/
3. The project currently has chromedriver version 80.0.3987.106. If this doesn't match your current chrome version, download a suitable chromedriver version from https://chromedriver.chromium.org/downloads. Place the driver inside the drivers directory, named as 'chromedriver': Quote-Scraper/src/drivers/chromedriver. 
4. Navigate to the src directory and run QuoteScraper.py
```
python3 QuoteScraper.py
```
