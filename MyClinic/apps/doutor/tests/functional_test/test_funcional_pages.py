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
    def test_list_doc_done_appointment_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        exam = wait.until(
            EC.presence_of_element_located((By.ID, "list_complete_appointment"))
        )
        exam.click()
        sleep(5)

        browser.quit()

    def test_list_doc_done_exam_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        exam = wait.until(EC.presence_of_element_located((By.ID, "list_complete_exam")))
        exam.click()
        sleep(5)

        browser.quit()

    def test_list_create_and_emit_medical_leave_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(
            EC.presence_of_element_located((By.ID, "list_medical_leave"))
        )
        leave.click()
        sleep(2)
        criar = wait.until(EC.presence_of_element_located((By.ID, "leave_form")))
        criar.click()
        patient = browser.find_element(By.NAME, "patient")
        patient.send_keys("Teste")
        sleep(1)
        days = browser.find_element(By.NAME, "days")
        days.send_keys(2)
        sleep(1)
        date = browser.find_element(By.NAME, "date")
        date.send_keys("12/02/2023")
        sleep(4)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, "submit")))
        BtnRequest.click()
        sleep(5)
        detail = browser.find_element(By.ID, "leave_detail")
        browser.execute_script("arguments[0].click()", detail)
        sleep(5)

        browser.quit()

    def test_list_and_detail_appointment_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(EC.presence_of_element_located((By.ID, "list_appointment")))
        leave.click()
        sleep(5)
        detail = browser.find_element(By.ID, "appointment_detail")
        browser.execute_script("arguments[0].click()", detail)
        sleep(5)

        browser.quit()

    def test_list_appointment_view_conclude_appointment_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(EC.presence_of_element_located((By.ID, "list_appointment")))
        leave.click()
        sleep(5)
        clear = browser.find_element(By.ID, "conclude_appointment")
        browser.execute_script("arguments[0].click()", clear)
        sleep(5)
        browser.quit()

    def test_list_exam_view_and_conclude_exam_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(EC.presence_of_element_located((By.ID, "list_exam")))
        leave.click()
        sleep(5)
        clear = browser.find_element(By.ID, "conclude_exam")
        browser.execute_script("arguments[0].click()", clear)
        sleep(5)
        browser.quit()

    def test_list_done_appointment_view_and_emit_prescription_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(
            EC.presence_of_element_located((By.ID, "list_complete_appointment"))
        )
        leave.click()
        sleep(5)
        clear = browser.find_element(By.ID, "prescription_detail")
        browser.execute_script("arguments[0].click()", clear)
        sleep(5)
        browser.quit()

    def test_list_done_appointment_view_and_emit_requisition_page(self):
        browser = webdriver.Chrome()
        browser.get("http://127.0.0.1:8000/medico_login/")
        wait = WebDriverWait(browser, 5)

        username = browser.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("Crash")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("clinica123")
        password.send_keys(Keys.RETURN)
        leave = wait.until(
            EC.presence_of_element_located((By.ID, "list_complete_appointment"))
        )
        leave.click()
        sleep(5)
        clear = browser.find_element(By.ID, "exam_detail")
        browser.execute_script("arguments[0].click()", clear)
        sleep(5)
        browser.quit()
