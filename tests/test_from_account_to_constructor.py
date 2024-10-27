from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_from_account_to_constructor(user, driver, registration, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text()='Конструктор']")))
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_from_account_to_constructor_by_logo(user, driver, registration, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")))
    driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
