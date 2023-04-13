import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com')
    assert driver.title == "Google"
    driver.quit()

def test_Insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()

def test_whatsapp():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.whatsapp.com')
    assert driver.title == "WhatsApp"
    driver.quit()
