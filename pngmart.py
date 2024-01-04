# Scrape pngmart (#02):

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

sitemap = "https://www.pngmart.com/sitemap.xml"
main_response = requests.get(sitemap)

xml = requests.get(sitemap).text
main_soup = bs(xml, "xml")

sitemaps = []

for loc in main_soup.find_all("loc"): 
  url = loc.text
  # print(url)

  if "posts" in url: 
    # print(url)
    sitemaps.append(url)

sitemap1 = sitemaps[0]
response1 = requests.get(sitemap1).text
soup1 = bs(response1, "xml")

master_list = []
for loc in soup1.find_all("loc"): 
  url = loc.text
  master_list.append(url)

# print(len(master_list))

for image_url in master_list[0:3]: 
  print(image_url)
  response2 = requests.get(image_url).text
  soup2 = bs(response2, "html.parser")

  image_id = image_url.split("/")[-1]
  # download_class = soup2.find_all("a", {"class": "download"}) # So.. There Is Just One a Tag With Download class
  png_url = soup2.find("a", {"class": "download"})["href"]
  print(png_url)

  image = requests.get(png_url)
  image_title = image_id + "-" + png_url.split("/")[-1] # Make It Any Name

  with open(image_title, "wb") as file:
    file.write(image.content)
    print("Done.")

  # break

