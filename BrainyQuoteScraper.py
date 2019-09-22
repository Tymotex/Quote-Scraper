from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
import os
import requests


def quote_scraper(category, quote_amount):
    # Navigates to site and identifies relevant element
    browser = webdriver.Chrome(executable_path="C:\\Gecko\\chromedriver.exe")
    browser.get(category_dict.get(category.title()))
    picture_elements = browser.find_elements_by_css_selector(".oncl_q img")
    quote_elements = browser.find_elements_by_css_selector("a[title='view quote']")
    pprint.pprint(quote_elements)
    for i in quote_elements:
        print(i.text)
    # Saves text and image
    quote_text_file = open("C:\\My Python Programs\\BrainyQuotes\\" + category.title() + "_quotes.txt", "w")
    quote_counter = 0
    while quote_counter < quote_amount:
        for each_quote in quote_elements:
            quote_text_file.write(each_quote.text + "\n")
            quote_counter += 1
            print(category.title() + " quotes gathered: " + str(quote_counter))
            if quote_counter >= quote_amount:
                break
        for each_image in picture_elements[quote_counter:]:  # picture_elements is the LIST of all relevant web elements. Starting from quote_counter prevents the picture elements from downloading at the beginning. This happens because not all content is loaded upfront, this needs to be revealed through scrolling down.
            # Downloading Pictures
            picture_url = "https://www.brainyquote.com" + each_image.get_attribute("data-img-url")
            picture_response = requests.get(picture_url)
            picture_response.raise_for_status()
            picture_file_name = os.path.basename(picture_url)  # This is the name of the image!
            picture = open(downloads_folder + "\\" + picture_file_name, "wb")
            for chunk in picture_response.iter_content(100000):
                picture.write(chunk)

        html_element = browser.find_element_by_css_selector("html")
        html_element.send_keys(Keys.END)
        quote_elements = browser.find_elements_by_css_selector("a[title='view quote']")
        picture_elements = browser.find_elements_by_css_selector(".oncl_q img")

    quote_text_file.close()
    quote_text_file2 = open("C:\\My Python Programs\\BrainyQuotes\\" + category.title() + "_quotes.txt", "r")
    print("Quotes in text file: ", str(len(quote_text_file2.readlines())))
    print("Process completed!")


category_dict = {
    "Age": "https://www.brainyquote.com/topics/age",
    "Alone": "https://www.brainyquote.com/topics/alone",
    "Amazing": "https://www.brainyquote.com/topics/amazing",
    "Anger": "https://www.brainyquote.com/topics/anger",
    "Anniversary": "https://www.brainyquote.com/topics/anniversary",
    "Architecture": "https://www.brainyquote.com/topics/architecture",
    "Art": "https://www.brainyquote.com/topics/art",
    "Attitude": "https://www.brainyquote.com/topics/attitude",
    "Beauty": "https://www.brainyquote.com/topics/beauty",
    "Best": "https://www.brainyquote.com/topics/best",
    "Birthday": "https://www.brainyquote.com/topics/birthday",
    "Brainy": "https://www.brainyquote.com/topics/brainy",
    "Business": "https://www.brainyquote.com/topics/business",
    "Car": "https://www.brainyquote.com/topics/car",
    "Chance": "https://www.brainyquote.com/topics/chance",
    "Change": "https://www.brainyquote.com/topics/change",
    "Christmas": "https://www.brainyquote.com/topics/christmas",
    "Communication": "https://www.brainyquote.com/topics/communication",
    "Computers": "https://www.brainyquote.com/topics/computers",
    "Cool": "https://www.brainyquote.com/topics/cool",
    "Courage": "https://www.brainyquote.com/topics/courage",
    "Dad": "https://www.brainyquote.com/topics/dad",
    "Dating": "https://www.brainyquote.com/topics/dating",
    "Death": "https://www.brainyquote.com/topics/death",
    "Design": "https://www.brainyquote.com/topics/design",
    "Diet": "https://www.brainyquote.com/topics/diet",
    "Dreams": "https://www.brainyquote.com/topics/dreams",
    "Easter": "https://www.brainyquote.com/topics/easter",
    "Education": "https://www.brainyquote.com/topics/education",
    "Environmental": "https://www.brainyquote.com/topics/environmental",
    "Equality": "https://www.brainyquote.com/topics/equality",
    "Experience": "https://www.brainyquote.com/topics/experience",
    "Failure": "https://www.brainyquote.com/topics/failure",
    "Faith": "https://www.brainyquote.com/topics/faith",
    "Family": "https://www.brainyquote.com/topics/family",
    "Famous": "https://www.brainyquote.com/topics/famous",
    "Father's Day": "https://www.brainyquote.com/topics/fathersday",
    "Fear": "https://www.brainyquote.com/topics/fear",
    "Finance": "https://www.brainyquote.com/topics/finance",
    "Fitness": "https://www.brainyquote.com/topics/fitness",
    "Food": "https://www.brainyquote.com/topics/food",
    "Forgiveness": "https://www.brainyquote.com/topics/forgiveness",
    "Freedom": "https://www.brainyquote.com/topics/freedom",
    "Friendship": "https://www.brainyquote.com/topics/friendship",
    "Funny": "https://www.brainyquote.com/topics/funny",
    "Future": "https://www.brainyquote.com/topics/future",
    "Gardening": "https://www.brainyquote.com/topics/gardening",
    "God": "https://www.brainyquote.com/topics/god",
    "Good": "https://www.brainyquote.com/topics/good",
    "Government": "https://www.brainyquote.com/topics/government",
    "Graduation": "https://www.brainyquote.com/topics/graduation",
    "Great": "https://www.brainyquote.com/topics/great",
    "Happiness": "https://www.brainyquote.com/topics/happiness",
    "Health": "https://www.brainyquote.com/topics/health",
    "History": "https://www.brainyquote.com/topics/history",
    "Home": "https://www.brainyquote.com/topics/home",
    "Hope": "https://www.brainyquote.com/topics/hope",
    "Humor": "https://www.brainyquote.com/topics/humor",
    "Imagination": "https://www.brainyquote.com/topics/imagination",
    "Independence": "https://www.brainyquote.com/topics/independence",
    "Inspirational": "https://www.brainyquote.com/topics/inspirational",
    "Intelligence": "https://www.brainyquote.com/topics/intelligence",
    "Jealousy": "https://www.brainyquote.com/topics/jealousy",
    "Knowledge": "https://www.brainyquote.com/topics/knowledge",
    "Leadership": "https://www.brainyquote.com/topics/leadership",
    "Learning": "https://www.brainyquote.com/topics/learning",
    "Legal": "https://www.brainyquote.com/topics/legal",
    "Life": "https://www.brainyquote.com/topics/life",
    "Love": "https://www.brainyquote.com/topics/love",
    "Marriage": "https://www.brainyquote.com/topics/marriage",
    "Medical": "https://www.brainyquote.com/topics/medical",
    "Memorial Day": "https://www.brainyquote.com/topics/memorialday",
    "Men": "https://www.brainyquote.com/topics/men",
    "Mom": "https://www.brainyquote.com/topics/mom",
    "Money": "https://www.brainyquote.com/topics/money",
    "Morning": "https://www.brainyquote.com/topics/morning",
    "Mother's Day": "https://www.brainyquote.com/topics/mothersday",
    "Motivational": "https://www.brainyquote.com/topics/motivational",
    "Movies": "https://www.brainyquote.com/topics/movies",
    "Moving On": "https://www.brainyquote.com/topics/movingon",
    "Music": "https://www.brainyquote.com/topics/music",
    "Nature": "https://www.brainyquote.com/topics/nature",
    "New Year's": "https://www.brainyquote.com/topics/newyears",
    "Parenting": "https://www.brainyquote.com/topics/parenting",
    "Patience": "https://www.brainyquote.com/topics/patience",
    "Patriotism": "https://www.brainyquote.com/topics/patriotism",
    "Peace": "https://www.brainyquote.com/topics/peace",
    "Pet": "https://www.brainyquote.com/topics/pet",
    "Poetry": "https://www.brainyquote.com/topics/poetry",
    "Politics": "https://www.brainyquote.com/topics/politics",
    "Positive": "https://www.brainyquote.com/topics/positive",
    "Power": "https://www.brainyquote.com/topics/power",
    "Relationship": "https://www.brainyquote.com/topics/relationship",
    "Religion": "https://www.brainyquote.com/topics/religion",
    "Respect": "https://www.brainyquote.com/topics/respect",
    "Romantic": "https://www.brainyquote.com/topics/romantic",
    "Sad": "https://www.brainyquote.com/topics/sad",
    "Saint Patrick's Day": "https://www.brainyquote.com/topics/saintpatricksday",
    "Science": "https://www.brainyquote.com/topics/science",
    "Smile": "https://www.brainyquote.com/topics/smile",
    "Society": "https://www.brainyquote.com/topics/society",
    "Space": "https://www.brainyquote.com/topics/space",
    "Sports": "https://www.brainyquote.com/topics/sports",
    "Strength": "https://www.brainyquote.com/topics/strength",
    "Success": "https://www.brainyquote.com/topics/success",
    "Sympathy": "https://www.brainyquote.com/topics/sympathy",
    "Teacher": "https://www.brainyquote.com/topics/teacher",
    "Technology": "https://www.brainyquote.com/topics/technology",
    "Teen": "https://www.brainyquote.com/topics/teen",
    "Thankful": "https://www.brainyquote.com/topics/thankful",
    "Thanksgiving": "https://www.brainyquote.com/topics/thanksgiving",
    "Time": "https://www.brainyquote.com/topics/time",
    "Travel": "https://www.brainyquote.com/topics/travel",
    "Trust": "https://www.brainyquote.com/topics/trust",
    "Truth": "https://www.brainyquote.com/topics/truth",
    "Valentine's Day": "https://www.brainyquote.com/topics/valentinesday",
    "Veterans Day": "https://www.brainyquote.com/topics/veteransday",
    "War": "https://www.brainyquote.com/topics/war",
    "Wedding": "https://www.brainyquote.com/topics/wedding",
    "Wisdom": "https://www.brainyquote.com/topics/wisdom",
    "Women": "https://www.brainyquote.com/topics/women",
    "Work": "https://www.brainyquote.com/topics/work",
}
selected_category = input("Type the category you want (from above): ")
amount_of_quotes = int(input("Enter how many quotes you want (int): "))
downloads_folder = "C:\\My Python Programs\\BrainyQuotes\\" + selected_category.title()
os.makedirs(downloads_folder, exist_ok=True)
quote_scraper(selected_category, amount_of_quotes)
