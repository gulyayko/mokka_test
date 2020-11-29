import pytest
from selenium import webdriver

from pages.base_page import BasePage
from environment.config import GetConfig as config


@pytest.fixture(scope="module")
def driver(request):
    capabilities = {
        "browserName": "chrome",
        "enableVNC": True,
        "enableVideo": False
    }
    webdriver_url = config().get('environment', 'webdriver_url')
    driver = webdriver.Remote(command_executor=webdriver_url, desired_capabilities=capabilities)
    driver.maximize_window()
    server_url = config().get('environment', 'host')
    driver.get(server_url)
    request.addfinalizer(driver.quit)
    return BasePage(driver).reset(driver)
