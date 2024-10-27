from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_logout(user, driver, registration, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Выход']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//h2[text()='Вход']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()
