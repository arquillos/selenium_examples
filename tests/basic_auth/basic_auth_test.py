'''
Created on Nov 10, 2019

@author: Arquillos
'''
import pytest

PAGE_TEXT = 'Congratulations! You must have the proper credentials.'
PAGE_TEXT_XPATH = '/html/body/div[2]/div/div/p'
PAGE_TITLE = 'The Internet'


@pytest.mark.usefixtures('setup')
class TestBasicAuth:
    '''
    Simple checks with Selenium
    '''
    def test_page_title(self):
        '''
        Check the title page after login with Basic Auth
        '''
        page_title = self.driver.title
        assert page_title == PAGE_TITLE

    def test_page_text(self):
        '''
        Check the page text after login with Basic Auth
        '''
        page_text = self.driver.find_element_by_xpath(PAGE_TEXT_XPATH).text
        assert page_text == PAGE_TEXT
