import os.path
import sys, time
import traceback
#locals:
from Action import (Action, ActionResult)
parentPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from init_webdriver import BrowserFactory

class IpCheckAction(Action):
    def __init__(self, *args, **kwargs):
        super(IpCheckAction, self).__init__(*args, **kwargs)

    def execute(self):
        """
        https://www.myip.com/
        <span id="ip">83.220.239.165</span>
        """
        self.browser.get('https://www.myip.com/')
        self.browser.set_page_load_timeout(10)
        if (not self.sleepTillLoaded()):
            return ActionResult(error='myip.com page not loaded')
        els = self.browser.find_elements_by_css_selector('[id="ip"]')
        if (not len(els)):
            return ActionResult(error='span#ip not found')
        el = els[0]
        ip = el.text.strip()
        return ActionResult(result={'ip':ip})

def main():
    """
    easy test
    """
    browser = None
    try:
        browser = BrowserFactory().getInstance()
        a = IpCheckAction(browser=browser)
        res = a.run()
        print(res.result)
        time.sleep(7)
    except Exception as e:
        None
        traceback.print_exc()
    finally:
        if 'WebDriver' in type(browser).__name__:
            browser.quit()


if '__main__' == __name__:
    main()
