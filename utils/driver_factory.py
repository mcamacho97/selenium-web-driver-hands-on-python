from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def get_web_driver(browser: str = "chrome") -> WebDriver:

    browser = browser.lower()
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browsers = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }

    if browser not in browsers:
        raise ValueError(f"Unsupported browser: {browser}")

    return browsers[browser](options=options)
