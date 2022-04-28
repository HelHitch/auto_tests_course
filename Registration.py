import imp
from ntpath import join
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

driver = webdriver.Chrome()

link = 'http://suninjuly.github.io/registration2.html'

try:
    driver.get(link)
    letters = string.ascii_letters
    random.seed(10)

    inputs = driver.find_elements(By.CSS_SELECTOR, "input[required]")
    for input in inputs:
        input.send_keys(''.join(random.choice(string.ascii_letters) for letters in range(10)))
   
    btn = driver.find_element(By.TAG_NAME, 'button').click()

        


finally:
    time.sleep(5)
    driver.quit()