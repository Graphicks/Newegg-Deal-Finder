from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/global/UK-en/todays-deals?cm_sp=Head_Navigation-_-Under_Search_Bar-_-Today%27s+Best+Deals&icid=650439'
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

all_items = {}
found_items = {}

class NewEgg():


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
            all_items[title] = price

        return all_items
    
    def find_items(all_items, item="", budget=0):
        for i in range(len(all_items)):
            item_price = (list(all_items.items()))[i][1]
            item_name = (list(all_items.keys()))[i]
                
            if budget >= float(item_price)  and item in item_name: 
                for y in range(len(all_items)):
                    found_items[item_name] = item_price
                
                                                
            elif item == "" and budget == 0:
                for y in range(len(all_items)):
                    found_items[item_name] = item_price
        return (found_items)
                               
