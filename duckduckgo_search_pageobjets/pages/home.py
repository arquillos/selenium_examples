'''
Created on Nov 14, 2019

@author: Arquillos

Page object class for DuckDuckGo home page
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoHomePage:
    URL = 'https://duckduckgo.com'
    # Locator
    SEARCH_BOX = (By.ID, 'search_form_input_homepage')

    def __init__(self, web_browser):
        self.web_browser = web_browser
    
    def load(self):
        self.web_browser.get(self.URL)

    def search(self, term):
        search_box = self.web_browser.find_element(*self.SEARCH_BOX)
        search_box.send_keys(term, Keys.RETURN)