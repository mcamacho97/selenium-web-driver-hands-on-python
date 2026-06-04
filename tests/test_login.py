from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
def test_failed_login(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login("test_user", "test_failed")
    
    assert driver.current_url == "https://www.saucedemo.com/"