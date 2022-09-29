import requests
from bs4 import BeautifulSoup

def check_flexwheels(sku):

    # Set our constants
    URL = "https://www.vexrobotics.com/vrc-flex-wheels.html"

    # Get the page from requests
    page = requests.get(URL)

    # Parse the html to find all of the elements which contain the items stock
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.find_all("td", attrs={"class" : "col qty"})

    # set a value for later
    final_item = ""

    # Loop through every single item on the page and find the exact one we looking for
    for item in items:
        for child in item.previous_sibling.previous_sibling:
            if sku in child:
                final_item = item

    # Check if the out of stock div is present if it is print out of stock else print in stock
    if final_item.contents[1].get("class") == ["stock", "unavailable"]:
        return 1
    else:
        return 0