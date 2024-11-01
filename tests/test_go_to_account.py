from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_account_button, locator_profile_link


class TestGoToAccount:

    def test_go_to_account(self, user, driver, login):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_profile_link)))

        assert driver.current_url == Url.url_profile_page
