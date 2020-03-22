from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
import os
import requests
import logging
import pickle

# Paths:
WEBDRIVER_PATH = "./drivers/chromedriver"
OUTPUT_PATH = "./Quotes/"

# URLs:
BASE_URL = "https://www.brainyquote.com"

# Configuration
logging.basicConfig(level=logging.INFO)


def quote_scraper(category, quote_amount, output_folder):
    """
        Given a category and number of quotes specified, opens a new 
        chrome browser process, navigates to the quote site and scrapes
        all quotes under that category from top-down. The quotes are 
        written to files in 
    """
    
    # Navigating to the site and identifying relevant elements
    logging.info("Navigating to {0}".format(category_dict.get(category.title())))
    browser = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
    browser.get(category_dict.get(category.title()))
    picture_elements = browser.find_elements_by_css_selector("div.qll-bg")
    quote_elements = browser.find_elements_by_css_selector("a[title='view quote']")
    
    # Saving text and image
    quote_text_file = open(output_folder + "/quotes.txt", "w")
    quote_counter = 0
    while quote_counter < quote_amount:
        for each_quote in quote_elements:
            quote_text_file.write("- " + each_quote.text + "\n")
            quote_counter += 1
            print(category.title() + " quotes gathered: " + str(quote_counter))
            if quote_counter >= quote_amount:
                break
        
        # picture_elements is the list of all relevant web elements for scraping
        # Starting from quote_counter prevents the picture elements from 
        # downloading at the beginning. This happens because not all content is 
        # loaded upfront. They need to be revealed by scrolling down.
        for each_image in picture_elements[quote_counter:]:  
            # Downloading Pictures
            try:
                picture_url = BASE_URL + each_image.get_attribute("data-img-url")
                picture_response = requests.get(picture_url)
                picture_response.raise_for_status()
                picture_file_name = os.path.basename(picture_url) 
                picture = open(output_folder + "/" + picture_file_name, "wb")
                logging.info("Fetching picture")
                for chunk in picture_response.iter_content(100000):
                    picture.write(chunk)
            except:
                pass
        
        # Force scroll down by sending END keystrokes to reveal further quotes 
        # on the next loop
        html_element = browser.find_element_by_css_selector("html")
        html_element.send_keys(Keys.END)
        quote_elements = browser.find_elements_by_css_selector("a[title='view quote']")
        picture_elements = browser.find_elements_by_css_selector(".oncl_q img")
    
    logging.info("Done scraping! See the results in {0}".format(output_folder))
    quote_text_file.close()
    browser.close()

if __name__ == "__main__":
    category_file = open("data.bin", "rb")
    category_dict = pickle.load(category_file)
    pprint.pprint(list(category_dict.keys()), width=100)
    selected_category = str(input("Type the category you want (from above): ")).capitalize()
    amount_of_quotes = int(input("Enter how many quotes you want (int): "))
    downloads_folder = OUTPUT_PATH + selected_category.title()
    os.makedirs(downloads_folder, exist_ok=True)
    quote_scraper(selected_category, amount_of_quotes, downloads_folder)
