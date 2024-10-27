from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration(user, driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

def test_registration_password_error(user, driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('12345')
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))

    assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").text == 'Некорректный пароль'

    driver.quit()
