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
    def test_admin_login_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        sleep(5)

        browser.quit()

    def test_admin_list_and_create_doctor_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        medicos = wait.until(EC.presence_of_element_located((By.ID, 'list_doctor')))
        medicos.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, 'doctor_create')))
        criar.click()
        first_name = browser.find_element(By.NAME, "first_name")
        first_name.send_keys("Charles")
        sleep(1)
        last_name = browser.find_element(By.NAME, "last_name")
        last_name.send_keys("B.")
        sleep(1)
        username = browser.find_element(By.NAME, "username")
        username.send_keys("Boyle")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("charles@gmail.com")
        sleep(2)
        phone = browser.find_element(By.NAME, "phone")
        phone.send_keys("95487-1588")
        sleep(2)
        city = browser.find_element(By.NAME, "city")
        city.send_keys("Pau dos Ferros")
        sleep(1)
        specialization = browser.find_element(By.NAME, "specialization")
        select = Select(specialization)
        select.select_by_visible_text("Urologista")
        sleep(2)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("clinica123")
        sleep(1)
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("clinica123")
        sleep(1)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
        BtnRequest.click()
        sleep(5)

        browser.quit()
    
    def test_admin_list_and_create_recepcionist_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        recepcionista = wait.until(EC.presence_of_element_located((By.ID, 'list_recepcionist')))
        recepcionista.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, 'recepcionist_create')))
        criar.click()
        first_name = browser.find_element(By.NAME, "first_name")
        first_name.send_keys("Regina")
        sleep(1)
        last_name = browser.find_element(By.NAME, "last_name")
        last_name.send_keys("L.")
        sleep(1)
        username = browser.find_element(By.NAME, "username")
        username.send_keys("Regina")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("gina@gmail.com")
        sleep(2)
        phone = browser.find_element(By.NAME, "phone")
        phone.send_keys("95468-1458")
        sleep(2)
        city = browser.find_element(By.NAME, "city")
        city.send_keys("Pau dos Ferros")
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("clinica123")
        sleep(1)
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("clinica123")
        sleep(1)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
        BtnRequest.click()
        sleep(5)

        browser.quit()

    def test_admin_exibe_income_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        caixa = wait.until(EC.presence_of_element_located((By.ID, 'list_caixa')))
        caixa.click()
        sleep(5)
        browser.quit()

    def test_admin_list_and_create_category_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        expenses = wait.until(EC.presence_of_element_located((By.ID, 'list_categoria')))
        expenses.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, 'categoria_form')))
        criar.click()
        name = browser.find_element(By.NAME, "name")
        name.send_keys("Comida")
        sleep(1)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
        BtnRequest.click()
        sleep(5)

        browser.quit()

    def test_admin_create_excel_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        expenses = wait.until(EC.presence_of_element_located((By.ID, 'list_despesas')))
        expenses.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, 'export_excel')))
        criar.click()
        sleep(5)
     
        browser.quit()

    def test_admin_list_expense_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/admin_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Administrador")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        expenses = wait.until(EC.presence_of_element_located((By.ID, 'list_despesas')))
        expenses.click()
        sleep(5)

        browser.quit()
