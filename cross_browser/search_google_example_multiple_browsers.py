'''
Created on Nov 12, 2019

@author: Arquillos
'''
from time import sleep
from selenium import webdriver

WAIT_TIME = 5
GOOGLE_URL = 'http://www.google.com/'
GOOGLE_SEARCH_BOX_NAME = 'q'
SEARCH_TERM = 'Test blogs'

@pytest.mark.usefixtures("firefox_driver_init")
class Test_Search_Firefox(Basic_Firefox_Test):
    def test_search_term(self):
        self.driver.get(GOOGLE_URL)

        # Wait for user to see the page
        sleep(WAIT_TIME)

        # Search for term "Test blogs"
        google_search_box = self.driver.find_element_by_name(GOOGLE_SEARCH_BOX_NAME)
        google_search_box.send_keys(SEARCH_TERM)
        google_search_box.submit()

        # Wait for the user to see the results
        sleep(WAIT_TIME) 

@pytest.mark.usefixtures("chrome_driver_init")
class Test_URL_Chrome(Basic_Chrome_Test):
    def test_search_term(self):
        self.driver.get(GOOGLE_URL)

        # Wait for user to see the page
        sleep(WAIT_TIME)

        # Search for term "Test blogs"
        google_search_box = self.driver.find_element_by_name(GOOGLE_SEARCH_BOX_NAME)
        google_search_box.send_keys(SEARCH_TERM)
        google_search_box.submit()

        # Wait for the user to see the results
        sleep(WAIT_TIME) 
