import allure

from environment.pathes import Path as path
from environment.config import GetConfig as config
from pages.base_page import BasePage as page


class ForgotPasswordPage:

    @staticmethod
    def should_be_forgot_password_page(driver):
        with allure.step('Проверить открытие страницы восстановления пароля'):
            try:
                exp_url = f"{config().get('environment', 'host')}{path.forgot_password}"
                actual_url = page(driver).get_url_()
                assert actual_url == exp_url, f"Wrong page\nExpected url: {exp_url}\n  Actual url: {actual_url}"
            except AssertionError:
                page(driver).get_screenshot()
                raise
