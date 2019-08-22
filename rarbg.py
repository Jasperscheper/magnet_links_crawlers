from selenium import webdriver
from platform import system
from bs4 import BeautifulSoup
from re import compile as re_compile
from time import sleep
import os


class SeleniumCrawler(object):

    def __init__(self):
        if system() == "Windows":
            self.browser = webdriver.Chrome(
                "{0}chromedriver.exe".format(os.path.join(os.environ['HOME']))
            )
        else:
            self.browser = webdriver.Chrome("chromedriver")

    def get_page(self, url):
        try:
            self.browser.get(url)
            return self.browser.page_source
        except Exception:
            return

    def get_soup(self, html):
        if html is not None:
            soup = BeautifulSoup(html, 'lxml')
            return soup
        else:
            return

    def get_list(self):
        print("Enter/Paste your links")
        contents = []
        try:
            while True:
                line = input()
                if line:
                    contents.append(line)	
                else:
                    break
            return contents
        except Exception:
            print("Enter/Paste urls")
            exit(1)

    def get_magnets(self, soup):
        try:
            for link in soup.findAll('a', attrs={'href': re_compile("^magnet")}):
                return link['href']
        except Exception:
            return

    def worker(self):
        self.get_page("https://rarbg.to/threat_defence.php?")
        for url in self.get_list():
            print(self.get_magnets(self.get_soup(self.get_page(url))))
            sleep(0.5)


s = SeleniumCrawler()
s.worker()
