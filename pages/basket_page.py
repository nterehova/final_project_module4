import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
        
    def should_be_empty_cart_message(self):
        page_language = self.browser.find_element(*BasketPageLocators.language_option)
        empty_message = self.browser.find_element(*BasketPageLocators.basket_empty_message).text
        if page_language == " British English ":
            assert empty_message == " Your basket is empty. ", "There is no message about empty cart"
        elif page_language == " Русский ":
            assert empty_message == " Ваша корзина пуста. ", "There is no message about empty cart"
        else:
            return False
            
    
    def is_no_product_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_items_form), "There are some products in cart"

