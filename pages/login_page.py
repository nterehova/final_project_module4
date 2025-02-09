import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        url_check = current_url.find("login")
        print(url_check)
        assert url_check != -1, "Url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.reg_email_field)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.reg_password_field)
        password_field.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.reg_confirm_password_field)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.register_button)
        register_button.click()
        
