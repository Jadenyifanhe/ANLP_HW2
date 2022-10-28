import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from .BasicSpider import BasicSpider

class ACLSeries(BasicSpider):

    def __init__(self, opt):
        super(ACLSeries, self).__init__()
        self.opt = opt

    def get_content(self, url, year):

        page = self.get_page(url)
        soup = BeautifulSoup(page, 'lxml')
        tag = soup.select('#title a')[0]
        pdf_url = tag['href']
        title = tag.get_text().strip()
        print("pdf link:" + str(pdf_url))

        if '/' in title:
            title = title.replace('/', 'or')
        print("paper title:"+str(title))

        self.saveFile(pdf_url, title, year)










