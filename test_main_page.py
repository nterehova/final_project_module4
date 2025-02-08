import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import math


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_go_to_cart()
    page.is_no_product_in_cart()
    page.should_be_empty_cart_message()
    
        
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()

#def test_login_url(browser):
#    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_url()

#def test_login_form(browser):
#    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()
    
#def test_register_form(browser):
#    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()
