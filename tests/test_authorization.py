from pages.login_page import LoginPage as login_page


class TestAuthorization:

    def test_empty_login(self, driver):
        login_page.should_be_login_page(driver)
        login_page.click_enter(driver)
        login_page.check_login_error_message(driver)
        login_page.check_error_message_text(driver)
