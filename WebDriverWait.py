from ast import arguments
from cgitb import text
from importlib.resources import path
from lib2to3.pgen2 import driver
import math
from ntpath import join
from select import select
import string
from time import sleep
from tkinter import Button
from webbrowser import get
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

try: 
    driver = webdriver.Chrome()
    driver.get(link)
    driver.execute_script("window.scrollBy(0, 100);")
    price = WebDriverWait(driver,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    btn = driver.find_element(By.TAG_NAME, 'button').click()
    def calc(x):
        return str (math.log(abs(12*math.sin(x))))
    num = driver.find_element(By.ID, 'input_value').text
    x = int(num)
    answer = calc(x)
    answ = driver.find_element(By.ID, 'answer').send_keys(answer)
    sbmt = driver.find_element(By.CSS_SELECTOR,'[type = submit]').click()

finally:
    time.sleep(12)
    quit()                                      

