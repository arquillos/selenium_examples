'''
Created on Nov 10, 2019

@author: Arquillos

A fixture that will be shared across several tests
'''
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROME_PATH = 'D:\\Internet\\Slimjet\\slimjet.exe'
CHROMEDRIVER_PATH = 'ChromeDriver\\chromedriver.exe'
URL = 'the-internet.herokuapp.com/basic_auth'
CREDENTIALS = 'admin:admin'


# The Seelnium Webdriver session is created only once during the test session
@pytest.fixture(scope="session")
def setup(request):
    '''
    setUp and tearDown Code

    Creating a Selenium WebDriver to be reused in all the tests

    Closing the Selenium WebDriver when the tests are passed
    '''
    # setUp Code
    # Set Chrome alternative binary path
    options = Options()
    options.binary_location = CHROME_PATH
    # Set ChromeDriver path
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    driver.maximize_window()

    # Open start page
    driver.get('http://' + CREDENTIALS + '@' + URL)

    # request.cls.driver = driver
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)

    yield driver

    # tearDown Code - Close WebDriver
    driver.close()
    driver.quit()
