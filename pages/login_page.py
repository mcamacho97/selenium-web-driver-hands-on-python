from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "login_logo")
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

        self.wait_for_element(self.PAGE_TITLE)

    def login(self, user: str, password: str):

        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, password)
        self.wait_for_element(self.LOGIN_BTN)
        self.click(self.LOGIN_BTN)
