'''
Created on Nov 12, 2019

@author: Arquillos

Fixtures that will be shared across several tests
'''
from selenium import webdriver

FIREFOXDRIVER_PATH='ChromeDriver/geckodriver'
CHROMEDRIVER_PATH='ChromeDriver/chromedriver'

# Firefox and Chrome fixture
@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def driver_init(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    else:
        web_driver = webdriver.Firefox(executable_path=FIREFOXDRIVER_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
