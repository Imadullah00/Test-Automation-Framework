import time
from selenium.webdriver.common.by import By
from base.BaseDriver import Basedriver
from utilities.utils import Utils

FILTER_BY_NON_STOP = "//div[@class='filter-heading pr sticky full-width']//label[1]"
FILTER_BY_1_STOP = "//div[@class='filter-heading pr sticky full-width']//label[2]"
FILTER_BY_2_STOP = "//div[@class='filter-heading pr sticky full-width']//label[3]"
FILTER_RES = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stops')]"


class SearchFlightResults(Basedriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    def get_filter_by_nonstop_locator(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, FILTER_BY_NON_STOP)

    def get_filter_by_1_locator(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, FILTER_BY_1_STOP)

    def get_filter_by_2_locator(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, FILTER_BY_2_STOP)

    def filterResultsby1(self):
        self.get_filter_by_1_locator().click()
        time.sleep(5)
        print("fine till here")

    def filterResultsby2(self):
        self.get_filter_by_2_locator().click()
        time.sleep(5)
        print("fine till here")

    def filterResultsbyNonStop(self):
        self.get_filter_by_nonstop_locator().click()
        time.sleep(5)
        print("fine till here")

    def filterResults(self, fltr):
        if fltr == "1 Stop":
            self.filterResultsby1()

        elif fltr == "2 Stops":
            self.filterResultsby2()

        elif fltr == "Non Stop":
            self.filterResultsbyNonStop()

        else:
            print("Please provide valid filter")

    def get_filter_results(self):

        return self.driver.find_elements(By.XPATH, FILTER_RES)

