import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url
from locators import locator_register_button, locator_login_account_button, locator_login_button, locator_order_button


@pytest.fixture
def user():
    login = ''
    password = ''
    for i in range(6):
        login += random.choice(list('1234567890'))
        password += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    user = User(name = 'igor_shulmin', email = 'igor_shulmin_15_' + login[:3] + '@yandex.ru', password = password)

    return user

@pytest.fixture
def driver(user):
    driver = webdriver.Chrome()
    driver.maximize_window()

    return driver

    driver.quit()

@pytest.fixture
def registration(user, driver):
    driver.get(Url.url_register_page)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_register_button)))

    elements = driver.find_elements(By.TAG_NAME, "input")
    elements[0].send_keys(user.name)
    elements[1].send_keys(user.email)
    elements[2].send_keys(user.password)
    driver.find_element(By.XPATH, locator_register_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

@pytest.fixture
def login(user, driver, registration):
    driver.get(Url.url_main_page)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_account_button)))
    driver.find_element(By.XPATH, locator_login_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locator_login_button)))

    elements = driver.find_elements(By.TAG_NAME, "input")
    elements[0].send_keys(user.email)
    elements[1].send_keys(user.password)
    driver.find_element(By.XPATH, locator_login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locator_order_button)))
