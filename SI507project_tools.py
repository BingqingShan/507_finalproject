import requests
import json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
import csv

######

START_URL = "https://toolkits.dss.cloud/design/"
FILENAME = "finalproject_cache.json"

PROGRAM_CACHE = Cache(FILENAME)


def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data)
    return data

#######


main_page = access_page_data(START_URL)

main_soup = BeautifulSoup(main_page, features="html.parser")
hrefs = [a["href"] for a in main_soup.select('div.flip-container a[href]')]
# print(hrefs)

# clean duplicate data
seen = set()
all_links = []
for item in hrefs:
    if item not in seen:
        seen.add(item)
        all_links.append(item)
# print(all_links)

# for link in all_links:
# print(link)

page_data = access_page_data('https://toolkits.dss.cloud/design/method-card/1-on-1-interview/')
soup_of_page = BeautifulSoup(page_data, features="html.parser")

# all info in one page
def one_page():
    name = soup_of_page.find('div',{'class':'title'}).find('h1')
    print(name.text)


    tasks= soup_of_page.find('div',{'class':'card_text'}).find('p')
    print(tasks.text)


    #grasp data
    feature= soup_of_page.find('section',{'class':'card_ww'}).find_all('div')
    #when
    when=feature[0].find('p')
    print(when.text)
    #why
    why=feature[1].find('p')
    print(why.text)
    #note
    note=feature[2].find('p')
    print(note.text)
    #output
    output=feature[3].find('p')
    print(output.text)
    #next
    next=feature[4].find('p')
    print(next.text)

#
# one_page_rows=zip(Name,Type,Description,Location,State)
#
# with open('test.csv', "a") as f:
#     writer = csv.writer(f)
#     for row in one_page_rows:
#         writer.writerow(row)
#
#
#
# topics_pages = []
# for l in all_links:
#     link='https://www.nps.gov'+l['href']
#     page_data = access_page_data(link)
#     soup_of_page = BeautifulSoup(page_data, features="html.parser")
#     # print(soup_of_page)
#     # topics_pages.append(soup_of_page)
#     # state=soup_of_page.find('h1').text
#     # print(state)
#     one_page()
