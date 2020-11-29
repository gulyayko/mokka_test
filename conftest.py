import pytest
from selenium import webdriver

from pages.base_page import BasePage
from environment.config import GetConfig as config


@pytest.fixture(scope="module")
def driver(request):
    # driver = webdriver.Chrome()
    capabilities = {
        "browserName": "chrome",
        "enableVNC": True,
        "enableVideo": False
    }
    driver = webdriver.Remote(command_executor="http://34.107.8.158:4444/wd/hub", desired_capabilities=capabilities)
    driver.maximize_window()
    server_url = config().get('environment', 'host')
    driver.get(server_url)
    request.addfinalizer(driver.quit)
    return BasePage(driver).reset(driver)
