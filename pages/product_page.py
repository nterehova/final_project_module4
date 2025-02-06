import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.add_to_cart_button)
        button.click()
        #self.solve_quiz_and_get_code()

    def should_be_message_about_added_product(self):
        assert self.is_element_present(*ProductPageLocators.message_product_added_to_cart), "Product is not added"
    
    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name)
        return product_name.text
        
    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price)
        return product_price.text
        
    def should_be_correct_product_added(self):
        #product_name = self.browser.find_element(*ProductPageLocators.product_name)
        product_name = self.return_product_name()
        product_name_in_message = self.browser.find_element(*ProductPageLocators.product_name_in_success_message)
        assert product_name == product_name_in_message.text, "Wrong product added to cart"
        
    def should_be_message_with_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.message_total_cart_price), "There is no success message with price"
    
    def should_be_correct_price_in_message(self):
        #product_price = self.browser.find_element(*ProductPageLocators.product_price)
        product_price = self.return_product_price()
        cart_price_in_message = self.browser.find_element(*ProductPageLocators.cart_price_in_message)
        assert product_price == cart_price_in_message.text, "Cart price is correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.message_product_added_to_cart), "Success message is presented, but should not be"
    
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.message_product_added_to_cart), "Success message has not disappeared, but should"
