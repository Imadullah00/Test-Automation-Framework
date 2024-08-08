import pytest
from pages.search_flights_results_page import SearchFlightResults
from pages.yatra_launch_page import LaunchPage
from selenium.webdriver.common.by import By
from utilities.utils import Utils
from selenium.webdriver.chrome.service import Service
import time


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def create_instance(self):
        self.launchp = LaunchPage(self.driver, self.wait)
        self.compare = Utils()
        print("called")
        # self.sf_results = SearchFlightResults(self.driver, self.wait)


    def test_search_flights(self):

       # self.launchp = LaunchPage(self.driver, self.wait)

        self.launchp.departFrom("New Delhi")

        self.launchp.goingTo("New York")

        self.launchp.selectDate("09/08/2024")

        self.launchp.ClickSearch()

        self.launchp.scroll_page()

        sf_results = SearchFlightResults(self.driver, self.wait)

        sf_results.filterResults("2 Stops")

        all_stops = sf_results.get_filter_results()
        print(len(all_stops))

        self.compare.assertTextfromList(all_stops, "2 Stops")
        print("end of first test")

    # def test_search_flights_2(self):
    #     print("In second test")
    #     #self.launchp = LaunchPage(self.driver, self.wait)
    #
    #     self.launchp.departFrom("New Delhi")
    #
    #     self.launchp.goingTo("New York")
    #
    #     self.launchp.selectDate("09/08/2024")
    #
    #     self.launchp.ClickSearch()
    #
    #     self.launchp.scroll_page()
    #
    #     sf_results = SearchFlightResults(self.driver, self.wait)
    #
    #     sf_results.filterResults("1 Stop")
    #
    #     all_stops = sf_results.get_filter_results()
    #     print(len(all_stops))
    #
    #     self.compare.assertTextfromList(all_stops, "1 Stop")