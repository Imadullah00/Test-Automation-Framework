import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request, browser):

    # chrome_install = ChromeDriverManager().install()
    # folder = os.path.dirname(chrome_install)
    # chromedriver_path = os.path.join(folder, "chromedriver.exe")
    # chrome_service = Service(chromedriver_path)
    #
    # driver = webdriver.Chrome(service=chrome_service)

    if browser == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == "firefox":
        s = Service(GeckoDriverManager.install())
        driver = webdriver.Firefox(service = s)
    elif browser == "edge":
        # s = EdgeService(EdgeChromiumDriverManager.install())
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        print("Invalid browser choice")

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope = "session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
