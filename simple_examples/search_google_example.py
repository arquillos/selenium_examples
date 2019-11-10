'''
Created on Nov 23, 2019

@author: Arquillos
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


WAIT_TIME = 5
CHROME_PATH = 'D:\\Internet\\Slimjet\\slimjet.exe'
CHROMEDRIVER_PATH = 'ChromeDriver\\chromedriver.exe'
GOOGLE_URL = 'http://www.google.com/'
GOOGLE_SEARCH_BOX_NAME = 'q'
SEARCH_TERM = 'Test blogs'

# Set Chrome alternative binary path
options = Options()
options.binary_location = CHROME_PATH
# Set ChromeDriver path
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

# Open Google start page
driver.get(GOOGLE_URL)

# Wait for user to see the page
time.sleep(WAIT_TIME) 

# Search for term "Test blogs"
google_search_box = driver.find_element_by_name(GOOGLE_SEARCH_BOX_NAME)
google_search_box.send_keys(SEARCH_TERM)
google_search_box.submit()

# Wait for the user to see the results
time.sleep(WAIT_TIME) 

# Close WebDriver
driver.quit()
