from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def get_web_driver(browser: str = "chrome") -> WebDriver:

    browser = browser.lower()

    browsers = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }

    if browser not in browsers:
        raise ValueError(f"Unsupported browser: {browser}")

    return browsers[browser]()
