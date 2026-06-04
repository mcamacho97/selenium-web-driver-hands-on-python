import pytest

from utils.execution_context import ExecutionContext
from utils.driver_factory import get_web_driver


@pytest.fixture(scope="session")
def execution_context():
    return ExecutionContext()


@pytest.fixture
def driver(execution_context):
    driver = get_web_driver()
    yield driver
    driver.quit()
