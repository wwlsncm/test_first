import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class NetworkPage(BaseAction):
    more_button = By.XPATH,"text,更多,1"
    network_button = By.XPATH,"text,移动网络,1"
    first_network_button = By.XPATH,"text,首选网络类型,1"
    net_2g_button = By.XPATH,"text,2G,1"
    net_3g_button = By.XPATH,"text,3G,1"
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    def click_more(self):
        self.click(self.more_button)
    def click_network(self):
        self.click(self.network_button)
    def click_first_network(self):
        self.click(self.first_network_button)
    def net_2g(self):
        self.click(self.net_2g_button)
    def net_3g(self):
        self.click(self.net_3g_button)