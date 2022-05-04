import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class testRegistration(unittest.TestCase):
    def test_registration(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        driver.get(link1)

        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your first name']").send_keys('name')
        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your email']").send_keys('email')
        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your last name']").send_keys('last_name')
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(3)
        txt = driver.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(txt, 'Congratulations! You have successfully registered!', 'False')

    def test_registration1(self):
        link2 = "http://suninjuly.github.io/registration2.html"

        driver.get(link2)

        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your first name']").send_keys('name')
        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your email']").send_keys('email')
        driver.find_element(By.CSS_SELECTOR, "[Placeholder= 'Input your last name']").send_keys('last_name')
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(3)
        txt = driver.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(txt, 'Congratulations! You have successfully registered!', 'True')


if __name__ == "__main__":
    unittest.main()
