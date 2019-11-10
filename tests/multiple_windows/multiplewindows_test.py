'''
Created on 10 February, 2019

@author: Arquillos
'''
import pytest


@pytest.mark.usefixtures('setup')
class TestNewWindow:
    '''
    Simple checks with Selenium
    '''
    def test_dropdown(self):
        '''
        Check the new opened window
        '''
        URL = 'http://the-internet.herokuapp.com/windows'

        # Open start page
        self.driver.get(URL)

        # Window page title
        print('Original page title: {}'.format(self.driver.title))

        # Find link to new page
        link = self.driver.find_element_by_link_text('Click Here')
        link.click()

        # Find new page 
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print('New window title: {}'.format(self.driver.title))

        assert self.driver.find_element_by_xpath('/html/body/div/h3').text == 'New Window'