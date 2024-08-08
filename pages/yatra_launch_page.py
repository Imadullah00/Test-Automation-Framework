import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.BaseDriver import Basedriver
from pages.search_flights_results_page import SearchFlightResults


class LaunchPage(Basedriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    LOCATION_LIST = "//div[@class='viewport']//div[1]//div[1]//li"
    DATE_FIELD =  "//input[@id='BE_flight_origin_date']"
    CALENDAR_TABLE = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def get_depart_from_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DEPART_FROM_FIELD)))

    def get_going_to_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GOING_TO_FIELD)))

    def get_location_list(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LOCATION_LIST))).find_elements(By.XPATH, self.LOCATION_LIST)

    def get_date_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DATE_FIELD)))

    def get_calendar_table(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.CALENDAR_TABLE))).find_elements(By.XPATH,  self.CALENDAR_TABLE)

    def get_search_btn(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON)))
    # ------------------------------------------------------------------------------------------------------

    def departFrom(self, departfromloc):
        depart_from = self.get_depart_from_field()
        depart_from.click()
        depart_from.send_keys(departfromloc)
        depart_from.send_keys(Keys.ENTER)

    def goingTo(self, goingto):

        going_to = self.get_going_to_field()
        going_to.click()
        time.sleep(2)
        going_to.send_keys(goingto)
        # going_to.send_keys(Keys.ENTER)
        time.sleep(2)
        # res = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]//div[1]")))
        res = self.get_location_list()
        time.sleep(2)
        print((len(res)))
        for options in res:
            if "New York (JFK)" in options.text:
                print(options.text)
                options.click()
                break

    def selectDate(self, dep_date):
        self.get_date_field().click()
        all_dates = self.get_calendar_table()
        for date in all_dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == dep_date:
                print("in if block")
                date.click()
                break

    def ClickSearch(self):

        self.get_search_btn().click()
        time.sleep(4)

