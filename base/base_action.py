from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(by,value))
    def find_elements(self,loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_elements(by,value))
    def click(self,loc):
        self.find_element(loc).click()
    def send_key(self,loc,text):
        self.find_element(loc).send_keys(text)
    def make_xpath_with_feature(self,loc):
        feature_start= "//*["
        feature_end = "]"
        feature = ""
        if isinstance(loc,str):
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_with_unitfeature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_with_unitfeature(i)
        feature = feature.rstrip("and")
        loc = feature_start + feature + feature_end
        return loc
    def make_xpath_with_unitfeature(self,loc):
        args = loc.split(",")
        feature = ""
        key_index = 0
        value_index = 1
        option_index = 2
        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ","  +"'"+ args[value_index] + "')" + "and"
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "=" +"'" + args[value_index] + "'" + "and"
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ","  +"'"+ args[value_index] + "')" + "and"
        return  feature