from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def could_add_to_basket(self):
        self.should_be_basket_button()
        self.add_to_basket()
        # self.test_message_disappeared_after_adding_product_to_basket()
        # self.guest_cant_see_success_message()
        # self.test_guest_cant_see_success_message_after_adding_product_to_basket()
        # self.solve_quiz_and_get_code()
        self.name_of_product_check()

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        # self.solve_quiz_and_get_code()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add to basket button doesn't exist"

    def name_of_product_check(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert  product_name == product_name_message, 'Name of added book is wrong!'

    def price_of_product_check(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_product_price, 'Price is wrong!'

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message isn't deisapear, but should be"