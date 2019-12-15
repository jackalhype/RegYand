import time, random
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse

class Action:
    def __init__(self, browser=None, *args, **kwargs):
        self.browser = browser
        self.info_list = []

    def run(self, *args, **kwargs):
        """
        @return ActionResult
        """
        return self.execute(*args, **kwargs)

    def execute(self, *args, **kwargs):
        """
        redefine in siblings
        """
        pass

    def actionResult(self, *args, **kwargs):
        """
        the only way to get correct ActionResult with execution info
        """
        info = ' \n'.join(self.info_list)
        ar = ActionResult(info=info, *args, **kwargs)
        return ar

    def info(self, msg):
        """
        push string to log stack
        """
        self.info_list.append(str(msg))

    def pageHasLoaded(self):
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'

    def sleepTillLoaded(self, previous_url='dull', max_seconds=14):
        for i in range(max_seconds * 2):
            time.sleep(0.5)
            if (previous_url == self.browser.current_url):
                continue
            if self.pageHasLoaded():
                return True
        return False

    def moveToElem(self, elem, xmax=31, ymax=15, xmin=1, ymin=1):
        """
        Move mouse, as smoothly as you can
        @param elem WebElement
        @params xmax, ymax, xmin, ymin pixels
        """
        None
        act = ActionChains(self.browser)
        p = self.randomPoint(xmax, ymax, xmin, ymin)
        act.move_to_element_with_offset(elem, p['x'], p['y'])
        act.pause(random.uniform(0.5, 0.9))
        act.perform()

    def randomPoint(self, xmax=31, ymax=15, xmin=1, ymin=1):
        x = int(random.uniform(xmin, xmax + 1))
        y = int(random.uniform(ymin, ymax + 1))
        return {'x': x, 'y': y, 0: x, 1: y}

    def getCurrentPath(self):
        url = self.browser.current_url
        o = urlparse(url)
        return o.path

class ActionResult:
    def __init__(self, success=True, error=None, result=None, info=None):
        """
        @param success bool
        @param error str
        @param result mixed
        """
        self.error = error
        if (error == None):
            self.success = success
        else:
            self.success = False
        self.result = result
        self.info = info
