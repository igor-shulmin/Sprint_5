from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_constructor_title_sousy, locator_constructor_title_bulki, \
    locator_constructor_current_div_bulki, locator_constructor_current_div_sousy, locator_constructor_title_nachinki, \
    locator_constructor_current_div_nachinki


class TestConstructor:

    def test_constructor_bulki(self, driver):
        driver.get(Url.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_constructor_title_sousy)))
        driver.find_element(By.XPATH, locator_constructor_title_sousy).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_constructor_title_bulki)))
        driver.find_element(By.XPATH, locator_constructor_title_bulki).click()

        element = driver.find_element(By.XPATH, locator_constructor_current_div_bulki)
        assert 'type_current' in element.get_attribute("class")

    def test_constructor_sousy(self, driver):
        driver.get(Url.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_constructor_title_sousy)))
        driver.find_element(By.XPATH, locator_constructor_title_sousy).click()

        element = driver.find_element(By.XPATH, locator_constructor_current_div_sousy)
        assert 'type_current' in element.get_attribute("class")

    def test_constructor_nachinki(self, driver):
        driver.get(Url.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_constructor_title_nachinki)))
        driver.find_element(By.XPATH, locator_constructor_title_nachinki).click()

        element = driver.find_element(By.XPATH, locator_constructor_current_div_nachinki)
        assert 'type_current' in element.get_attribute("class")
