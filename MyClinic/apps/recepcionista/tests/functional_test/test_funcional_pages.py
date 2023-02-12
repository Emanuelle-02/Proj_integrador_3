import os
import time
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class FunctionalTest(TestCase, LiveServerTestCase):
    def test_recepcionist_login_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/recepcionista_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Yuri")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        sleep(5)
        browser.quit()
