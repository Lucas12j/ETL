from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, re

class ScraperS():

    def __init__(self, url, cssSelector, regex = '.+', sleepTime = 1) -> None:

        self.cssSelectorErro = False
        self.regex = regex
        option = Options()
        option.headless = True
        self.driver = webdriver.Firefox(options = option, executable_path="/driver/geckodriver", service_log_path="/driver/geckodriver.log")
        self.driver.get(url)
        time.sleep(sleepTime)
        try:
            if isinstance(cssSelector, list):
                self.values = [self.driver.find_element_by_css_selector(i).get_attribute('outerHTML') for i in cssSelector]
            else:
                self.value = self.driver.find_element_by_css_selector(cssSelector).get_attribute('outerHTML')
        except Exception as e:
            print(repr(e))
            self.cssSelectorErro = True
        finally:
            self.driver.close()

    def getValue(self):
        if self.cssSelectorErro:
            return "Selenium CSS Selector Error", 410
        value = re.findall(self.regex, self.value)
        if len(value) == 0:
            return "SyntaxError Regex", 406
        elif len(value) == 1:
            return value[0],200
        elif len(value) > 1:
            return value, 200

    def getValues(self):
        if self.cssSelectorErro:
            return "Selenium CSS Selector Error", 410
        values = [re.findall(i[0], i[1])[0] for i in zip(self.regex, self.values)]
        return values, 200

