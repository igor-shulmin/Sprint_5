locator_register_button = ".//button[text()='Зарегистрироваться']" # кнопка регистрации
locator_register_text_uncorrect_password = ".//p[text()='Некорректный пароль']" # сообщение об ошибке при регистрации

locator_login_button = ".//button[text()='Войти']" # кнопка входа
locator_login_account_button = ".//button[text()='Войти в аккаунт']" # кнопка входа в аккаунт
locator_account_button = ".//p[text()='Личный Кабинет']" # переход в личный кабинет
locator_login_from_register_and_forgot_button = ".//a[text()='Войти']" # переход на авторизацию с других страниц

locator_order_button = ".//button[text()='Оформить заказ']" # кнопка оформления заказа

locator_profile_link = ".//a[text()='Профиль']" # переход в профиль

locator_constructor_link = ".//p[text()='Конструктор']" # переход в Конструктор
locator_logo_link = ".AppHeader_header__logo__2D0X2" # переход в Конструктор по клику на логотип
locator_constructor_text = ".//h1[text()='Соберите бургер']" # заголовок Конструктора

locator_logout_button = ".//button[text()='Выход']" # кнопка выхода

locator_constructor_title_bulki = ".//span[text()='Булки']" # заголовок раздела "Булки"
locator_constructor_title_sousy = ".//span[text()='Соусы']" # заголовок раздела "Соусы"
locator_constructor_title_nachinki = ".//span[text()='Начинки']" # заголовок раздела "Начинки"

# переход к актуальному разделу Конструктора
locator_constructor_current_div_bulki = ".//*[contains(text(),'Булки')]/parent::div[contains(@class, 'type_current')]"
locator_constructor_current_div_sousy = ".//*[contains(text(),'Соусы')]/parent::div[contains(@class, 'type_current')]"
locator_constructor_current_div_nachinki = ".//*[contains(text(),'Начинки')]/parent::div[contains(@class, 'type_current')]"
