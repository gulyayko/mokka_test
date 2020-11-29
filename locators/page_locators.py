class CommonLocators:
    back_link = 'xpath', '//a[text()="Вернуться назад"]'
    confirm_button = 'xpath', '//button[text()="Продолжить"]'
    error_message = 'css', '.formBlock__errorMessage'
    main_logo = 'css', '.login__logo'
    phone_input = 'css', '#mobile_phone'


class LoginPageLocators:
    activate_link = 'xpath', '//a[text()="Активировать профиль?"]'
    enter_button = 'css', '[name="commit"]'
    forgot_link = 'xpath', '//a[text()="Забыли пароль?"]'
    password_input = 'css', '#password'
    login_error_msg = 'xpath', '//div[text()="Неправильный логин или пароль"]'


class ResetPasswordPageLocators:
    reset_phone_input = 'css', '#login'
