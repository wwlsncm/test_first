import os,sys
sys.path.append(os.getcwd())
from appium import webdriver
from base.base_driver import init_driver
from page.network_page import NetworkPage
class TestNetwork:
    def setup(self):
        self.d = init_driver()
        self.network_page = NetworkPage(self.d)
    def test_setting_2g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.net_2g()
    def test_setting_3g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.net_3g()
