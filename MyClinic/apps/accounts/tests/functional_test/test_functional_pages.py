from time import sleep

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class FunctionalTest(TestCase, LiveServerTestCase):
    def test_admin_show_login_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")
        wait = WebDriverWait(browser, 3)
        sleep(2)
        register = wait.until(EC.presence_of_element_located((By.ID, "login")))
        register.click()
        sleep(3)
        browser.quit()

    def test_show_doctor_login_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")
        wait = WebDriverWait(browser, 3)
        sleep(2)
        register = wait.until(EC.presence_of_element_located((By.ID, "login_doctor")))
        register.click()
        sleep(3)
        browser.quit()

    def test_show_recepcionist_login_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/")
        wait = WebDriverWait(browser, 3)
        sleep(2)
        register = wait.until(
            EC.presence_of_element_located((By.ID, "login_recepcionist"))
        )
        register.click()
        sleep(3)
        browser.quit()
