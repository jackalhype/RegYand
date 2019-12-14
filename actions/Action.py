import time

class Action:
    def __init__(self, browser=None, *args, **kwargs):
        self.browser = browser

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

    def pagehasLoaded(self):
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'

    def sleepTillLoaded(self, max_seconds=14):
        for i in range(max_seconds * 2):
            time.sleep(0.5)
            if self.pagehasLoaded():
                return True
        return False

class ActionResult:
    def __init__(self, success=True, error=None, result=None):
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
