'''
Created on Nov 14, 2019

@author: Arquillos
'''
import pytest
from selenium import webdriver

WAIT_TIME_SEGS = 10


@pytest.fixture
def init_chrome_browser():
    driver = webdriver.Chrome()

    # Wait for Chrome to startup
    driver.implicitly_wait(WAIT_TIME_SEGS)

    yield driver

    driver.close()
    driver.quit()
