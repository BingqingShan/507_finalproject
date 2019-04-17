import requests, json
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
list_of_topics = main_soup.find_all('div',{'class':'flip-container'})
print(list_of_topics) # cool
#
# all_links = list_of_topics.find_all('a')
# print(all_links) # cool
#
#
# for link in all_links:
#     print(link['href'])
#
#
#
# # test on one page
# page_data = access_page_data('https://www.nps.gov/state/mi/index.htm')
# soup_of_page = BeautifulSoup(page_data, features="html.parser")
#
#
# #all info in one page
# def one_page():
#     Location=[]
#     location=soup_of_page.find_all('h4')
#     for i in location[1:]:
#         # print(i.text)
#         Location.append(i.text)
#         # print(Location)
#
#     Description=[]
#     description=soup_of_page.find_all('p')
#     for i in description[:-2]:
#         # print(i.text)
#         Description.append(i.text[1:-1])
#         # print(Description)
#
#     Name=[]
#     name=soup_of_page.find_all('h3')
#     for i in name[1:]:
#         item=i.find('a')
#         if item != None:
#             Name.append(item.text)
#     # print(Name)
#
#
#
#     Type=[]
#     type=soup_of_page.find_all('h2')
#     for i in type[1:-2]:
#         Type.append(i.text)
#         # print(i.text)
#     # print(Type)
#
#
#     numbers=len(name)-1
#
#     State=[]
#     state=soup_of_page.find('h1').text
#     for i in range(0,numbers):
#         # print(i.text)
#         State.append(state)
#     # print(State)
#
#     one_page_rows=zip(Name,Type,Description,Location,State)
#
#     with open('test.csv', "a") as f:
#         writer = csv.writer(f)
#         for row in one_page_rows:
#             writer.writerow(row)
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
