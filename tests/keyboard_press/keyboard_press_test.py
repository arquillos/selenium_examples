'''
Created on 21 March, 2019

@author: Arquillos
'''
import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('setup')
class TestNewWindow:
    '''
    Simple checks with Selenium
    '''
    def test_dropdown(self):
        '''
        Check the new opened window
        '''
        url = 'http://the-internet.herokuapp.com/key_presses'

        # Open start page
        self.driver.get(url)

        # Locate element - 'body' and send Key " "
        self.driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)

        # Localte element - id result and check the text
        assert self.driver.find_element_by_id('result').text == 'You entered: SPACE'
