from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:/Users/shash/Documents/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(
            executable_path="C:/Users/shash/Documents/drivers/chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# PyTest HTML reports


# hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopcommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shashank'


# hook for deleting/modifying environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)