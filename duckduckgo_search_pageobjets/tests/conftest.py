'''
Created on Nov 14, 2019

@author: Arquillos
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Lib import json
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys

CHROMEDRIVER_PATH='ChromeDriver\\chromedriver.exe'
CHROME_PATH = 'D:\\Internet\\Slimjet\\slimjet.exe'
FIREFOXDRIVER_PATH='FirefoxDriver\\\geckodriver.exe'
FIREFOX_PATH = 'D:\\Internet\\FirefoxPortable\\App\\Firefox64\\Firefox.exe'


@pytest.fixture
def config(scope='session'):
    # Read the configuration file
    with open('duckduckgo_search_pageobjets\\config.json') as config_file:
        config = json.load(config_file)

    # Check for valid file values
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def web_browser(config):
    # setUp Code
    options = Options()

    if config['browser'] == 'Firefox':
        # Set Firefox alternative binary path
        driver = webdriver.Firefox(executable_path=FIREFOXDRIVER_PATH,
                                   firefox_binary=FirefoxBinary(FIREFOX_PATH))
    elif config['browser'] == 'Chrome':
        # Set Chrome alternative binary path
        options.binary_location = CHROME_PATH
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    elif config['browser'] == 'Headless Chrome':
        options.add_argument('headless')
        options.binary_location = CHROME_PATH
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    else:
        raise Exception(f"Browser not supported: {config['browser']}")

    # Wait for browser to startup
    driver.implicitly_wait(config['implicit_wait'])

    yield driver

    # tearDown Code - Close WebDriver
    driver.close()
    driver.quit()
