#! /usr/bin/env python3

import mechanize
from bs4 import BeautifulSoup


class visite(object):

    def __init__(self, url, user_agent, proxy=None) -> None:
        if url.endswith("/"):
                 self.url = url.rstrip("/") 
        else:
             self.agent = user_agent
             self.br = mechanize.Browser()      
             self.all_link = []

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
    

    def get_link(self, url):
        if url is None:
             url = self.url
        page_source = self.view_page(url)
        if page_source is not None:
             soup = BeautifulSoup(page_source, "html_parser")