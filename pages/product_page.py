from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .locators import ProductPageLocators


class ProductPage(BasePage):
    

    def guest_can_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()
        self.solve_quiz_and_get_code()

        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text, 'цена совпадает'

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text, 'название совпадает'