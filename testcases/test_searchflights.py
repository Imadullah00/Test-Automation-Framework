import pytest
from pages.search_flights_results_page import SearchFlightResults
from pages.yatra_launch_page import LaunchPage
from selenium.webdriver.common.by import By
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack
import unittest
from selenium.webdriver.chrome.service import Service
import time


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def create_instance(self):
        self.launchp = LaunchPage(self.driver, self.wait)
        self.compare = Utils()
        print("called")
        # self.sf_results = SearchFlightResults(self.driver, self.wait)

    # @data(("New Delhi", "New York", "19/08/2024", "2 Stops"), ("Mumbai", "New York", "20/08/2024", "1 Stop"))
    # @unpack

    @file_data("../testdata/test_injson.json")
    def test_search_flights(self, goingfrom, goingto, date, stops):

       # self.launchp = LaunchPage(self.driver, self.wait)

        self.launchp.departFrom(goingfrom)

        self.launchp.goingTo(goingto)

        self.launchp.selectDate(date)

        self.launchp.ClickSearch()

        self.launchp.scroll_page()

        sf_results = SearchFlightResults(self.driver, self.wait)

        sf_results.filterResults(stops)

        all_stops = sf_results.get_filter_results()
        print(len(all_stops))

        self.compare.assertTextfromList(all_stops, stops)
        print("end of first test")

