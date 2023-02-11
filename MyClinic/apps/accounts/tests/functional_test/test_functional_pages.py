from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.

class FunctionalTest(LiveServerTestCase):
    driver = webdriver.Chrome()
    def test_main_navegation_register_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        
        assert "MyClinic - Página inicial" in self.browser.title
        
        about_link = self.browser.find_element(By.LINK_TEXT, 'op_login')
        about_link.click()
        
        assert "MyClinic" in self.browser.title
        
        pass