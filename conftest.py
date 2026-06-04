import pytest

from utils.driver_factory import get_web_driver


@pytest.fixture
def driver():
    driver = get_web_driver()
    yield driver
    driver.quit()
