from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    

    def guest_can_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()
        self.solve_quiz_and_get_code()

        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text, 'цена совпадает'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text, 'название совпадает'

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def message_disappeared_after_adding_produc(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
        