from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.test_guest_cant_see_product_in_basket()
        self.test_guest_can_see_basket_is_empty_text()

    def should_be_basket_url(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        assert 'basket' in self.browser.current_url, 'basket_url must have "basket" inside!!'

    def test_guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), 'The products are in the basket, but should not be'

    def test_guest_can_see_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), '"Basket is empty text" is present, but should not be'