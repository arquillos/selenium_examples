'''
Created on Nov 12, 2019

@author: Arquillos

Fixtures that will be shared across several tests
'''
import pytest
from selenium import webdriver

FIREFOXDRIVER_PATH='ChromeDriver/geckodriver'
CHROMEDRIVER_PATH='ChromeDriver/chromedriver'


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
    chrome_driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
    chrome_driver.quit()
