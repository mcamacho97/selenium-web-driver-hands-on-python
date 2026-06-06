from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver
from utils.execution_context import ExecutionContext



class EvidenceManager:
    def __init__(self, driver: WebDriver, execution_context: ExecutionContext) -> None:
        self.driver = driver

        self.execution_context = execution_context

    def save_screenshot(self, name: str) -> Path:
        screenshot_path = self.execution_context.screenshots_folder / f"{name}.png"

        self.driver.save_screenshot(str(screenshot_path))

        return screenshot_path

    def save_page_source(self, name: str) -> Path:
        source_path = self.execution_context.logs_folder / f"{name}.html"
        return source_path
