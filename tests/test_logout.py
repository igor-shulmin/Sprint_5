from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_account_button, locator_login_button, locator_logout_button


class TestLogout:

    def test_logout(self, user, driver, login):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_logout_button)))
        driver.find_element(By.XPATH, locator_logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        assert driver.current_url == Url.url_login_page

        driver.quit()
