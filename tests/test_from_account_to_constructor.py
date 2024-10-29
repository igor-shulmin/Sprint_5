from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_account_button, locator_constructor_link, locator_constructor_text, locator_logo_link


class TestFromAccountToConstructor:

    def test_from_account_to_constructor(self, user, driver, login):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_constructor_link)))
        driver.find_element(By.XPATH, locator_constructor_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_constructor_text)))

        assert driver.current_url == Url.url_main_page

    def test_from_account_to_constructor_by_logo(self, user, driver, login):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator_logo_link)))
        driver.find_element(By.CSS_SELECTOR, locator_logo_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_constructor_text)))

        assert driver.current_url == Url.url_main_page
