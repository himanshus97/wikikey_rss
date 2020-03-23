"""
rsstitle.py

Used to Extract data from RSS feeds using two techniques 
1. Regex - Regular Expressions
2. BeautifulSoup

references:
-> https://www.regextester.com/27540
-> https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-xml
"""

from bs4 import BeautifulSoup
import requests
import re
import datetime
import json
import os


# Fetch urls from databases or files. (Right I have just one link so HARDCODE it)
URLs = ['https://timesofindia.indiatimes.com/rssfeeds/1898055.cms']

#Fetch RSS Feed content using GET REQUEST 
def get_req_data(url,soup):
    if soup == 'soup':
        return requests.get(url).content
    else:
        return requests.get(url).text

#Process RSS Feed Content using BEAUTIFULSOUP
def get_soup_data(content,find_item):
    soup = BeautifulSoup(content,features="xml")
    found = soup.findAll(find_item)
    return [i.text for i in found]

#Process RSS Feed Content using Regular Expression 
def get_regex_data(content,find_item):
    tag = f"<\s*{find_item}[^>]*>(.*?)<\s*/\s*{find_item}>"
    found = re.findall(tag,content)
    return found

#Append the data into file according to day
def append_data(data):
    with open(f"./data/parsed_{datetime.date.today()}.txt",'a') as f:
        json.dump(data,f)
        f.write(os.linesep)

# main function for beautifulsoup
def soup():
    for url in URLs:
        fetch_data = {
            'link' : url,
            'titles' : (get_soup_data(get_req_data(url,'soup'),'title'))
            }
        append_data(fetch_data)

# main function for regex
def regex():
    for url in URLs:
        fetch_data = {
            'link' : url,
            'titles' : (get_regex_data(get_req_data(url,'regex'),'title'))
            }
        append_data(fetch_data)


