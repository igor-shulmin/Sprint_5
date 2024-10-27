from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_constructor_bulki():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//h2[text()='Булки']")))
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Булки']")))

    assert driver.find_element(By.XPATH, ".//span[text()='Булки']").text == 'Булки'

    driver.quit()

def test_constructor_sousy():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))

    assert driver.find_element(By.XPATH, ".//span[text()='Соусы']").text == 'Соусы'

    driver.quit()

def test_constructor_nachinki():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Начинки']")))

    assert driver.find_element(By.XPATH, ".//span[text()='Начинки']").text == 'Начинки'

    driver.quit()
