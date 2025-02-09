import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    basket_button = (By.CSS_SELECTOR, ".basket-mini a[href*='basket']")

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "form#login_form")
    register_form = (By.CSS_SELECTOR, "form#register_form")
    reg_email_field = (By.CSS_SELECTOR,"input#id_registration-email")
    reg_password_field = (By.CSS_SELECTOR, "input#id_registration-password1")
    reg_confirm_password_field = (By.CSS_SELECTOR, "input#id_registration-password2")
    register_button = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    add_to_cart_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    #изначальные вебэлементы с атрибутами продукта на странице
    product_name = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    product_price = (By.CSS_SELECTOR, "p.price_color")
    
    # название и цена продукта в сообщениях
    message_product_added_to_cart =(By.XPATH, "//*[@id='messages']/div[1]/div")
    product_name_in_success_message = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    message_total_cart_price =(By.XPATH, "//*[@id='messages']/div[3]/div/p[1]")
    cart_price_in_message = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    #корзина в хэдере
    mini_cart_in_header = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]")

class BasketPageLocators():
    basket_items_form = (By.CSS_SELECTOR, "form#basket_formset")
    basket_empty_message = (By.XPATH, "//*[@id='content_inner']/p")
    language_option = (By.CSS_SELECTOR, "select[name='language'] option[selected]")
