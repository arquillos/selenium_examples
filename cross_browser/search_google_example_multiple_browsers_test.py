'''
Created on 12 Nov, 2019

@author: Arquillos
'''
import pytest

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


WAIT_TIME = 5
GOOGLE_URL = 'http://www.google.com/'
GOOGLE_SEARCH_BOX_NAME = 'q'
SEARCH_TERM = 'Test blogs'
CHROMEDRIVER_PATH = 'ChromeDriver/chromedriver'
FIREFOXDRIVER_PATH = 'ChromeDriver/geckodriver'

# Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
    firefox_driver = webdriver.Firefox(executable_path=FIREFOXDRIVER_PATH)
    request.cls.driver = firefox_driver
    yield
    firefox_driver.close()
    firefox_driver.quit()

# Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    # Set ChromeDriver path
    chrome_driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
    chrome_driver.quit()

@pytest.mark.usefixtures("firefox_driver_init")
class Test_Search_Firefox():
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
class Test_URL_Chrome():
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
