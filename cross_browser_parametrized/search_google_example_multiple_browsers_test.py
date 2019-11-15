'''
Created on Nov 12, 2019

@author: Arquillos
'''
import pytest

from time import sleep
from selenium import webdriver

WAIT_TIME = 5
GOOGLE_URL = 'http://www.google.com/'
GOOGLE_SEARCH_BOX_NAME = 'q'
SEARCH_TERM = 'Test blogs'

@pytest.mark.usefixtures("driver_init")
class Test_Search_Browser():
    def test_search_term(self):
        # Given
        self.driver.get(GOOGLE_URL)
        sleep(WAIT_TIME)

        # When - Search for term "Test blogs"
        google_search_box = self.driver.find_element_by_name(GOOGLE_SEARCH_BOX_NAME)
        google_search_box.send_keys(SEARCH_TERM)
        google_search_box.submit()
        sleep(WAIT_TIME) 

        # Then
        link_divs = self.driver.find_elements_by_css_selector('#rso > div > div')
        assert len(link_divs) > 0
