import allure

from pages.base_page import BasePage as page
from locators.page_locators import LoginPageLocators as locator
from environment.config import GetConfig as config
from environment.pathes import Path as path


class LoginPage:

    @staticmethod
    def should_be_login_page(driver):
        with allure.step('Проверить открытие страницы логина'):
            try:
                exp_url = f"{config().get('environment', 'host')}{path.login}"
                actual_url = page(driver).get_url_()
                assert actual_url == exp_url, f"Wrong page\nExpected url: {exp_url}\n  Actual url: {actual_url}"
            except AssertionError:
                page(driver).get_screenshot()
                raise

    @staticmethod
    def click_forgot_password_link(driver):
        with allure.step('Кликнуть по ссылке "Забыли пароль?" и перейти на страницу восстановления пароля'):
            try:
                page(driver).click_(locator.forgot_link)
            except Exception:
                page(driver).get_screenshot()
                raise Exception('Не удалось кликнуть на ссылку "Забыли пароль"')

    @staticmethod
    def click_enter(driver):
        with allure.step('Кликнуть по кнопке "Вход"'):
            try:
                page(driver).click_(locator.enter_button)
            except Exception:
                page(driver).get_screenshot()
                raise Exception('Не удалось кликнуть на кнопку "Вход"')

    @staticmethod
    def check_login_error_message(driver):
        with allure.step("Проверить появление сообщения об ошибке входа"):
            try:
                assert page(driver).is_element_displayed(locator.login_error_msg), \
                    'Не появилось сообщение об ошибке входа'
            except AssertionError:
                page(driver).get_screenshot()
                raise

    @staticmethod
    def check_error_message_text(driver):
        with allure.step("Проверить текст сообщения об ошибке"):
            message = page(driver).get_element(locator.login_error_msg)
            try:
                assert message.text == 'Неправильный логин или пароль', 'Некорректный текст ошибки'
                page(driver).get_screenshot()
            except AssertionError:
                page(driver).get_screenshot()
                page(driver).remove_highlight(message)
                raise
