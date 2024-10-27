from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_main_by_button(user, driver, registration):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH,".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH,".//button[text()='Оформить заказ']").text == 'Оформить заказ'

    driver.quit()

def test_login_from_main_by_account(user, driver, registration):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text == 'Оформить заказ'

    driver.quit()

def test_login_from_registration(user, driver, registration):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH,".//button[text()='Оформить заказ']").text == 'Оформить заказ'

    driver.quit()

def test_login_from_forgot_password(user, driver, registration):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.find_element(By.XPATH,".//button[text()='Оформить заказ']").text == 'Оформить заказ'

    driver.quit()
