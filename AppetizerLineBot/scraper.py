from bs4 import BeautifulSoup
from abc import ABC, abstractclassmethod
import requests
import cloudscraper
from requests.api import head
import re

class Appetizer(ABC):

    def __init__(self, bangoo):
        self.bangoo = bangoo

    @abstractclassmethod
    def scrape(self):
        pass

class Avgle(Appetizer):

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            "Referer": "https://www.google.com/"
        }

        url = "https://avgle.com/search/videos?search_query="+ self.bangoo +"&search_type=videos"
        response = requests.get(url=url,headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all('a', href=re.compile("^/video/"), limit=5)
        if results == []:
            # print("來自Avgle的搜尋結果:\n查無結果")
            return "來自Avgle的搜尋結果:\n查無結果"

        links = ""
        for result in results:
            links += "https://avgle.com" + result.get('href') + "\n\n"
        # print("來自Avgle的搜尋結果:\n" + links)
        return "來自Avgle的搜尋結果:\n" + links

class Netflav(Appetizer):

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            "Referer": "https://www.google.com/"
        }

        url = "https://netflav.com/search?type=title&keyword=" + self.bangoo
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all('div', class_='grid_cell', limit=5)
        if results == []:
            # print("來自Netflav的搜尋結果:\n查無結果")
            return "來自Netflav的搜尋結果:\n查無結果"

        links = ""
        for result in results:
            a = result.find('a')
            links += "https://netflav.com" + a.get('href') + "\n\n"

        # print("來自Netflav的搜尋結果:\n" + links)
        return "來自Netflav的搜尋結果:\n" + links

class Av01(Appetizer):

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            "Referer": "https://www.google.com/"
        }
        
        url = "https://www.av01.tv/search/videos?search_query=" + self.bangoo
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all('a', href=re.compile('^/video/'),limit=5)
        if results == []:
            print("來自Av01的搜尋結果:\n查無結果")
            return "來自Av01的搜尋結果:\n查無結果"

        links = ""
        for result in results:
            links += "https://jp.av01.tv" + result.get('href') + "\n\n"

        print("來自Av01的搜尋結果:\n" + links)
        return "來自Av01的搜尋結果:\n" + links


if __name__ == "__main__":
    obj = Av01("mide-870")
    obj.scrape()



    # cookie = "splash-forapp=6; AVS=6jib09es1v8b28m9vmdgu7l161; splash-forapp=NaN; splash_i=false; _gid=GA1.2.2043691135.1641539608; _ga=GA1.2.1794721309.1641539607; _ga_SBSWMB7KCQ=GS1.1.1641539606.1.1.1641540042.0"
        # cookies = {}
        # for line in cookie.split(';'):
        #     key, value = line.strip().split('=', 1)
        #     cookies[key] = value