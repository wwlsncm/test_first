import os,sys
sys.path.append(os.getcwd())
from appium import webdriver
from base.base_driver import init_driver
from page.display_page import DisplayPage
class TestDisplay:
    def setup(self):
        self.d = init_driver()
        self.display_page = DisplayPage(self.d)
    def test_setting_search(self):
        self.display_page.click_search()
        self.display_page.input_text("hello")
        self.display_page.click_back()
        assert 0
