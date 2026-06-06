from pages.login_page import LoginPage


def test_successful_login_chrome(driver, evidence_manager):
    login_page = LoginPage(driver, evidence_manager)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_fail(driver, evidence_manager):

    driver.get("https://www.saucedemo.com")

    assert False


# def test_successful_login_firefox(driver):
#     firefox_driver = get_web_driver("firefox")

#     login_page = LoginPage(firefox_driver)

#     login_page.open()

#     login_page.login("standard_user", "secret_sauce")

#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"
