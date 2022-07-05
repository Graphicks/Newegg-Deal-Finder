from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/global/UK-en/todays-deals?cm_sp=Head_Navigation-_-Under_Search_Bar-_-Today%27s+Best+Deals&icid=650439'
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

all_items = {} # All the items found from the initial get_items
found_items = {} # All the items found after doing find_items

class NewEgg():


    def get_content(): # Navigates the HTML tree and returns the contents 
        page_content = (doc.find("div", {"class": "item-cells-wrap tile-cells five-cells"})).contents
        return page_content

    def get_items(page_content): # Looks through the contents to find the title and price of the product
        for table_rows in page_content[:30]:
            title = (table_rows.a.img['title'])
            price = (f"{table_rows.strong.string}{table_rows.sup.string}").replace(",", '') # Adds the strong price to the sup price and removes any commas, this allows us to convert into a float.
            all_items[title] = price # Stores the name and the price in a dictionary

        return all_items
    
    def find_items(all_items, item="", budget=0): # Looks through the items we got and finds deals based off the users desires
        for i in range(len(all_items)):
            item_price = (list(all_items.items()))[i][1] # The current price of the item we're looking at
            item_name = (list(all_items.keys()))[i] # The current name of the item we're looking at 
                
            if budget >= float(item_price)  and item in item_name: # If the budget is greater than the price of the item and the item is what we specified it will put that deal into a dictionary
                for y in range(len(all_items)):
                    found_items[item_name] = item_price
                
                                                
            elif item == "" and budget == 0: # If the user does not input a budget or item it will return all items in a dictionary 
                for y in range(len(all_items)):
                    found_items[item_name] = item_price
        return (found_items)
                            
