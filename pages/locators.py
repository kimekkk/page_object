from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.XPATH, '//p[@class="price_color"][1]')
    PRICE_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]//strong')