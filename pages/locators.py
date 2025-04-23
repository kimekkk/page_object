from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"  # Подстрока для проверки URL
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.XPATH, '//p[@class="price_color"][1]')
    PRICE_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class BasketPageLocators:
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")  # Более точный селектор
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p")
