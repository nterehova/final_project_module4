import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
import time
import math


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
