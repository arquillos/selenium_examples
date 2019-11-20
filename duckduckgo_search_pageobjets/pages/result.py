'''
Created on Nov 14, 2019

@author: Arquillos

Page object class for DuckDuckGo results page
'''
import logging

from selenium.webdriver.common.by import By

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


class DuckDuckGoResultPage:
    # Locators
    SEARCH_BOX = (By.ID, 'search_form_input')
    RESULTS_LINKS = (By.CSS_SELECTOR, 'a.result__a')

    def __init__(self, web_browser):
        self.web_browser = web_browser

    def result_link_titles(self):
        result_links = self.web_browser.find_elements(*self.RESULTS_LINKS)
        result_titles = [link.text for link in result_links]
        logging.info(f'Page result links titles: {result_titles}')
        return result_titles
  
    def search_input_value(self):
        search_box = self.web_browser.find_element(*self.SEARCH_BOX)
        search_box_value = search_box.get_attribute('value')
        logging.info(f'Search page input value: {search_box_value}')
        return search_box_value

    def title(self):
        logging.info(f'Page title: {self.web_browser.title}')
        return self.web_browser.title
