import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


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

@pytest.fixture
def registration(user, driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    return registration

@pytest.fixture
def login(user, driver, registration):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(user.email)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(user.password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    return login
