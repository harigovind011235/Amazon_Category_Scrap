from bs4 import BeautifulSoup
import requests
import json


def writemyjson(data):
    json_text = json.dumps(data,indent=8,sort_keys=True)
    with open('amazoncategories.json', 'a') as json_file:
        json_file.write(json_text)

myresponse = requests.get('https://www.amazon.in/gp/site-directory?ref=nav_em_ajax_fail')
myhtml = myresponse.text

soup = BeautifulSoup(myhtml,'lxml')

main_category_links = []
categories = []



for div in soup.select('.popover-grouping'):
    categoryname = [x.text for x in div.select('.popover-category-name')]
    categorylinks = [x.attrs['href'] for x in div.select('.nav_a')]
    categorydict = {'categoryname':categoryname,
                    'categorylinks':categorylinks}

    categories.append(categorydict)       #appending each dictionary to a list
    writemyjson(categories)



    main_category_links.append(categorylinks)   #making a list for make further requests
    # for subcategry in main_category_links:    # making requests to each category link
    #     mysubhtml = requests.get(subcategry)
    #     mysubhtml2 = BeautifulSoup(mysubhtml.text,'lxml')
    #     print(mysubhtml2)


