from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):

        self.wait_for_element(locator)

        self.driver.find_element(*locator).click()

    def type(self, locator, text):

        self.wait_for_element(locator)

        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):

        self.wait_for_element(locator)

        return self.driver.find_element(*locator).text
