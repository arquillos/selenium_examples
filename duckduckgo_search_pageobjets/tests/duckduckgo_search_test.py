'''
Created on Nov 14, 2019

@author: Arquillos

DuckDuckGo search test
'''
import pytest
import logging

from duckduckgo_search_pageobjets.pages.home import DuckDuckGoHomePage
from duckduckgo_search_pageobjets.pages.result import DuckDuckGoResultPage

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


@pytest.mark.parametrize('search_term', ['commodore', 'spectrum', 'amstrad'])
def test_duckduckgo_search(web_browser, search_term):
  # Given - DuckDuckGo home page is loaded
  ddg_search_page = DuckDuckGoHomePage(web_browser)
  ddg_result_page = DuckDuckGoResultPage(web_browser)
  logging.info(f'Loading DuckDuckGo home page')
  ddg_search_page.load()

  # When - Search for "Commodore"
  logging.info(f'Searching for term {search_term}')
  ddg_search_page.search(search_term)

  # Then - Search result page query has the search term
  logging.info(f'Checking the page search inout box value')
  assert search_term in ddg_result_page.search_input_value()

  # And - Search result links has the search term
  for title in ddg_result_page.result_link_titles():
    logging.info(f'Comparing page result: {title} with search term: {search_term}')
    assert search_term in title.lower()

  # And - Search result page title contains the search term
  logging.info(f'Checking the page title') 
  assert search_term in ddg_result_page.title()
