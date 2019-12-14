import os
import selenium
from selenium import webdriver
#local:
from conf_local import Config

class BrowserFactory:

    def __init__(self):
        self.config = config = Config()
        self.geckodriver = config['geckodriver']
        self.firefox_binary = config['firefox_binary']

    def getInstance(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--private")
        if not self.isWindows():
            firefox_options.add_argument("--headless")

        browser = webdriver.Firefox(
            executable_path=self.geckodriver,
            firefox_binary=self.firefox_binary,
            firefox_profile=firefox_profile,
            options=firefox_options
        )
        browser.set_window_position(0, 0)
        browser.set_window_size(1024, 768)
        return browser

    def isWindows(self):
        return os.name == 'nt'

def main():
    bf = BrowserFactory()
    browser = bf.getInstance()
    print(browser)
    browser.quit()

if '__main__' == __name__:
    main()
