import os,sys
import pytest
sys.path.append(os.getcwd())
from base.base_yaml import yaml_data_with_file
from base.base_driver import init_driver
from page.search_page import SearchPage
def data_with_key(key):
    return yaml_data_with_file("search_data")[key]
class TestSearch:
    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)
    @pytest.mark.parametrize("content",data_with_key("test_search"))
    def test_search(self,content):
        self.search_page.click_search()
        self.search_page.input_content(content)
        self.search_page.click_back()