'''
Created on Nov 10, 2019

@author: Arquillos
'''
import pytest
from selenium.common.exceptions import NoSuchElementException

PAGE_TEXT = 'Congratulations! You must have the proper credentials.'
PAGE_TEXT_XPATH = '/html/body/div[2]/div/div/p'
PAGE_TITLE = 'The Internet'


@pytest.mark.usefixtures('setup')
class TestCheckBoxes:
    '''
    Simple checks with Selenium
    '''
    def test_first_checkbox(self):
        '''
        Check the first checkbox state
        '''
        try:
            checkbox1_state = self.driver.find_element_by_tag_name('input').is_selected()
            assert not checkbox1_state
        except NoSuchElementException as exception:
            print(exception)

    def test_second_checkbox(self):
        '''
        Check the second checkbox state
        '''
        try:
            checkbox2_state = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[2]').is_selected()
            assert checkbox2_state
        except NoSuchElementException as exception:
            print(exception)
