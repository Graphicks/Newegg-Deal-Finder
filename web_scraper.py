from bs4 import BeautifulSoup
import requests

# User Inputs
item = input("What item are you looking for?    ")
budget = int(input("What is your budget?    "))


url = 'https://www.newegg.com/global/UK-en/todays-deals?cm_sp=Head_Navigation-_-Under_Search_Bar-_-Today%27s+Best+Deals&icid=650439'
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

fixed_prices = {}

class WebScraper():


    def get_html():
        app = (doc.find(id='app'))
        page_content = (app.find("div", {"class": "page-content"}))
        page_section = (page_content.find("section", {"class": "page-section is-gray-background"}))
        page_parent_div = (page_section.find("div", {"class": "page-section-inner"}))
        page_div = (page_parent_div.find("div", {"class": "item-cells-wrap tile-cells five-cells"}))

        page_div_contents = (page_div.contents)

        return page_div_contents

    def get_items(page_div_contents):
        for table_rows in page_div_contents[:30]:
            title = (table_rows.a.img['title'])
            price = (f"{table_rows.strong.string}{table_rows.sup.string}").replace(",", '')
            fixed_prices[title] = price

        return fixed_prices
    
    def find_items(fixed_prices, item="", budget=0):
        for i in range (len(fixed_prices)):

            item_price = (list(fixed_prices.items()))[i][1]
            item_name = (list(fixed_prices.keys()))[i]

            if float(item_price) <= budget and item in item_name: 

                print(f"\nFound {item_name} for £{item_price} on Newegg!\n") 
                
            elif item == "" and budget == 0:
                print(f"\nFound {item_name} for £{item_price} on Newegg!\n")     
                
        

page_div_contents = WebScraper.get_html()
items = (WebScraper.get_items(page_div_contents))
WebScraper.find_items(fixed_prices, item, budget)
