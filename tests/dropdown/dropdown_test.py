'''
Created on Nov 10, 2019

@author: Arquillos
'''
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('setup')
class TestCheckBoxes:
    '''
    Simple checks with Selenium
    '''
    def test_dropdown(self):
        '''
        Check the disabled element
        '''
        URL = 'http://the-internet.herokuapp.com/dropdown'

        # Open start page
        self.driver.get(URL)

        try:
            dropdown_element = self.driver.find_element_by_id('dropdown')
            select = Select(dropdown_element)
            options = select.options

            options_list = []

            for option in options: #iterate over the options, place attribute value in list
                options_list.append(option.get_attribute("value"))

            for option_value in options_list:
                print('starting loop on option {}'.format(option_value))

            # assert not checkbox1_state
        except NoSuchElementException as exception:
            print(exception)
