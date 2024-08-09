import time

class Basedriver:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self):
        pagelen = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
        match = False
        while match == False:
            lastcount = pagelen
            time.sleep(1)
            pagelen = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
            if lastcount == pagelen:
                match = True
        time.sleep(7)



