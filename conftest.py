import pytest
from selenium import webdriver

from pages.base_page import BasePage
from environment.config import GetConfig as config


@pytest.fixture(scope="module")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=capabilities)
    server_url = config().get('environment', 'host')
    driver.get(server_url)
    request.addfinalizer(driver.quit)
    return BasePage(driver).reset(driver)
