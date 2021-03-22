#import pymongo
import datetime
from bs4 import BeautifulSoup as bs
#from splinter import Browser
import numpy as py
import pandas as pd
import requests
import re

class Mars_Scraper:

    def scrape():
        return {
            'news' : this.get_news(),
            'featured': this.get_featured_image(),
            'stats': this.get_stats(),
            'locations': this.get_hemispheres()
            }

    def mars_news():
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        results = soup.find_all('div', class_='slide')
        latest = results[0]
        news_title = latest.select('div.content_title a')[0].text
        news_paragraph = latest.find('div', class_='rollover_description_inner').text
        return {
             'news_title': news_title, 
             'news_paragraph': news_paragraph
             }

#   def get_featured_image():
#         base_url = 'https://www.jpl.nasa.gov'
#         url = base_url + '/spaceimages/?search=&category=Mars'
#         browser.visit(url)
#         html = browser.html
#         soup = bs(html, 'html.parser')
#         b_image = soup.find('a', class_='button fancybox')
#         featured_image_url = base_url + b_image['data-fancybox-href']
#         return featured_image_url
  
    def get_stats():
        url = 'https://space-facts.com/mars/'
        tables = pd.read_html(url)
        mars_df = tables[0]
        html_table = mars_df.to_html()
        return html_table

    def get_hemispheres(): 
        main_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        base_url = 'https://astrogeology.usgs.gov'
        response = requests.get(main_url)
        soup = bs(response.text, 'html.parser')
        details = soup.find_all('a', class_='itemLink product-item')
        image_list = []
        for x in details:
            full_url = base_url + x['href']
            print(full_url)
            response = requests.get(full_url)
            soup = bs(response.text, 'html.parser')
            images = soup.find('a', string=re.compile('\.tif$'))
            image_list.append({'img_url':images['href'], 'title': soup.title.text})
            
        return image_list





 