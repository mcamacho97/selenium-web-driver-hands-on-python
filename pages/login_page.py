from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.evidence_manager import EvidenceManager

from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "login_logo")
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver: WebDriver, evidence_manager: EvidenceManager):
        self.driver = driver
        self.evidence_manager = evidence_manager

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

        self.evidence_manager.save_screenshot("login_page")
        self.evidence_manager.save_page_source("login_page")

        self.wait_for_element(self.PAGE_TITLE)

    def login(self, user: str, password: str):

        self.type(self.USERNAME, user)
        time.sleep(2)
        self.type(self.PASSWORD, password)
        time.sleep(2)
        self.wait_for_element(self.LOGIN_BTN)
        self.click(self.LOGIN_BTN)
        time.sleep(2)
