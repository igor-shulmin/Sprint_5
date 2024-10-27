from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_account(user, driver, registration, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//a[text()='Профиль']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.quit()
