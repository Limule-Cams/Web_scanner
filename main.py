#! /usr/bin/env python3

import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Visite(object):

    def __init__(self, url, user_agent, proxy=None) -> None:
        if url.endswith("/"):
                 self.url = url.rstrip("/") 
        else:
             self.agent = user_agent
             self.br = mechanize.Browser()      
             self.all_link = []
             self.url = url

    def view_page(self, url=None):
        if url is None:
            url = self.url
        url = url.strip()
        self.br.set_handle_robots(False)
        agent = [("user_agent", self.agent)]
        self.br.addheaders = agent
        try:
            content = self.br.open(url)
        except Exception as e:
             print("Erreur pour le page : "+ url + " "+ str(e))
        return content

    def all_link(self):
         for i in self.all_link:
              print(i)
    

    def get_link(self, url=None):
        list_link = []
        if url is None:
             url = self.url
        page_source = self.view_page(url)
        if page_source is not None:
             soup = BeautifulSoup(page_source, "html.parser")
             link_parse = urlparse(url)
             for l in soup.find_all("a"):
                  if l.get("href") is not None:
                       href = l.get("href")
                       if url.endswith("/"):
                            url = url.rstrip("/")
                       if len(href) > 0:
                            if link_parse.scheme+"://"+link_parse.hostname is not href and not href.startswith("http"):
                                 if not href.startswith("#") and not href.startswith("mailto"):
                                      if "#" in href:
                                           href = href.spit("#")[0]
                                      if href.startswith("/"):
                                            link_parse.scheme+"://"+link_parse.hostname+href
                                      else:
                                           href = url+"/"+href
                                      if href is not list_link:
                                           list_link.append(href)
                                           self.all_link.append(href)
                                           print(href)
                                
             return list_link
        else:
             return []

if __name__ == "__main__":
    a = Visite("https://google.com", "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0")
    a.get_link()
    a.all_link()