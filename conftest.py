import pytest

from utils.execution_context import ExecutionContext
from utils.driver_factory import get_web_driver
from utils.evidence_manager import EvidenceManager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        evidence_manager = item.funcargs.get("evidence_manager")

        if evidence_manager:
            evidence_manager.save_screenshot(f"{item.name}_FAILED")
            evidence_manager.save_page_source(f"{item.name}_FAILED")


@pytest.fixture(scope="session")
def execution_context():
    return ExecutionContext()


@pytest.fixture
def evidence_manager(driver, execution_context):
    return EvidenceManager(driver, execution_context)


@pytest.fixture
def driver(execution_context):
    driver = get_web_driver()
    yield driver
    driver.quit()
