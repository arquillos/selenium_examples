'''
Created on Nov 10, 2019

@author: Arquillos
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROME_PATH = 'D:\\Internet\\Slimjet\\slimjet.exe'
CHROMEDRIVER_PATH = 'ChromeDriver\\chromedriver.exe'
URL = 'http://the-internet.herokuapp.com/nested_frames'


# Set Chrome alternative binary path
options = Options()
options.binary_location = CHROME_PATH
# Set ChromeDriver path
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)

# Open start page
driver.get(URL)

# Change to top frame
driver.switch_to.frame('frame-top')
print('Switched to frame-top')

# Change to middle frame
driver.switch_to.frame('frame-middle')
print('Switched to frame-middle')

# Get text
text = driver.find_element_by_id('content').text
print('The text found is: {}'.format(text))

# Close WebDriver
driver.quit()
