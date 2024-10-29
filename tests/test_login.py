from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_login_account_button, locator_login_button, locator_order_button, locator_account_button, \
    locator_login_from_register_and_forgot_button


class TestLogin:

    def test_login_from_main_by_button(self, user, driver, registration):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_login_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.email)
        elements[1].send_keys(user.password)
        driver.find_element(By.XPATH, locator_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_order_button)))

        assert driver.find_element(By.XPATH,locator_order_button).text == 'Оформить заказ'

    def test_login_from_main_by_account(self, user, driver, registration):
        driver.get(Url.url_main_page)
        driver.find_element(By.XPATH, locator_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.email)
        elements[1].send_keys(user.password)
        driver.find_element(By.XPATH, locator_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_order_button)))

        assert driver.find_element(By.XPATH, locator_order_button).text == 'Оформить заказ'

    def test_login_from_registration(self, user, driver, registration):
        driver.get(Url.url_register_page)
        driver.find_element(By.XPATH, locator_login_from_register_and_forgot_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.email)
        elements[1].send_keys(user.password)
        driver.find_element(By.XPATH, locator_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_order_button)))

        assert driver.find_element(By.XPATH, locator_order_button).text == 'Оформить заказ'

    def test_login_from_forgot_password(self, user, driver, registration):
        driver.get(Url.url_forgot_password_page)
        driver.find_element(By.XPATH, locator_login_from_register_and_forgot_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.email)
        elements[1].send_keys(user.password)
        driver.find_element(By.XPATH, locator_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_order_button)))

        assert driver.find_element(By.XPATH, locator_order_button).text == 'Оформить заказ'
