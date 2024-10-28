from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators import locator_register_button, locator_login_button, locator_register_text_uncorrect_password


class TestRegistration:

    def test_registration(self, user, driver):
        driver.get(Url.url_register_page)

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.name)
        elements[1].send_keys(user.email)
        elements[2].send_keys(user.password)
        driver.find_element(By.XPATH, locator_register_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

        assert driver.current_url == Url.url_login_page

        driver.quit()

    def test_registration_password_error(self, user, driver):
        driver.get(Url.url_register_page)

        elements = driver.find_elements(By.TAG_NAME, "input")
        elements[0].send_keys(user.name)
        elements[1].send_keys(user.email)
        elements[2].send_keys('12345')
        driver.find_element(By.XPATH, locator_register_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_register_text_uncorrect_password)))

        assert driver.find_element(By.XPATH, locator_register_text_uncorrect_password).text == 'Некорректный пароль'

        driver.quit()
