from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def product_name_is_correct(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        message_about_adding = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT)
        print(product_name.text)
        print(message_about_adding.text)
        assert product_name.text == message_about_adding.text, "No product name in the message"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.CART_PRICE)
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "не равно"
