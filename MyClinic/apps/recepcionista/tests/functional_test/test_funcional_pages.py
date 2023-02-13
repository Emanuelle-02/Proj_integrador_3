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

    def test_list_and_create_exam_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/recepcionista_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Yuri")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        exam = wait.until(EC.presence_of_element_located((By.ID, 'exams_list')))
        exam.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, 'exam_form')))
        criar.click()
        patient = browser.find_element(By.NAME, "patient")
        patient.send_keys("Terry B.")
        sleep(1)
        age = browser.find_element(By.NAME, "age")
        age.send_keys("35")
        sleep(1)
        gender = browser.find_element(By.NAME, "gender")
        select = Select(gender)
        select.select_by_visible_text("Masculino")
        sleep(2)
        doctor = browser.find_element(By.NAME, "doctor")
        select = Select(doctor)
        select.select_by_visible_text("Holt R. - Cardiologista")
        sleep(2)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
        BtnRequest.click()
        sleep(5)

        browser.quit()