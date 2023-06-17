import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Opening chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Opening firefox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Opening edge browser")
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

@pytest.fixture(params=[
    ("rvshinde007@gmail.com", "007@Ravishinde", "Pass"),
    ("rvshinde009@gmail.com", "007@Ravishinde", "Fail"),
    ("rvshinde007@gmail.com", "001@Ravishinde" , "Fail"),
    ("rvshinde001@gmail.com", "006@Ravishinde", "Fail"),
])

def getDataForLogin(request):
    return request.param