import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

log = logging.getLogger()


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class BasePage:
    time = 5

    def __init__(self, driver):
        self.driver = driver

    def reset(self, driver):
        self.driver = driver
        return self

    def click_(self, locator):
        el = self._find_element(locator)
        self.highlight(el)
        el.click()
        log.info(f'click {locator}')

    def get_element(self, locator):
        el = self._find_element(locator)
        self.highlight(el)
        return el

    def highlight(self, element):
        self.driver.execute_script("arguments[0].style.border='2px dashed red'", element)

    def is_element_displayed(self, locator):
        return self._find_element(locator).is_displayed()

    def remove_highlight(self, element):
        self.driver.execute_script("arguments[0].style.border='none'", element)

    def get_url_(self):
        url = self.driver.current_url
        log.info(f'current url: {url}')
        return self.driver.current_url

    def get_screenshot(self):
        screen = self.driver.get_screenshot_as_png()
        allure.attach(screen, 'screenshot', allure.attachment_type.PNG)

    # private functions

    def _find_element(self, locator, timeout=time):
        """Ожидает и возвращает элемент после появления."""
        try:
            log.info(f'find_element{locator}')
            wait = WebDriverWait(self.driver, timeout)
            element = self._get_element_by_type(self.driver, locator)
            wait.until(EC.visibility_of(element))
            return element
        except TimeoutException:
            log.exception(f'Element with locator {locator} not found')
            raise TimeoutException(f'Element with locator {locator} not found')

    @staticmethod
    def _get_element_by_type(driver, locator):
        """Получает элемент методом, применимым для данного типа локатора."""
        el_type, value = locator
        if el_type == 'css':
            return driver.find_element_by_css_selector(value)
        if el_type == 'xpath':
            return driver.find_element_by_xpath(value)
        else:
            log.exception(f'Method {el_type} is not supported.')
            raise Exception(f'Method {el_type} is not supported.')

    # TODO: implement find_elements method
