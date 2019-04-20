import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class DisplayPage(BaseAction):
    display_button = By.XPATH,"//*[@text='显示']"
    search_button = By.ID,"com.android.settings:id/search"
    input_text_view = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.click(self.display_button)
    def click_search(self):
        self.click(self.search_button)
    def input_text(self,text):
        self.send_key(self.input_text_view,text)
    def click_back(self):
        self.click(self.back_button)