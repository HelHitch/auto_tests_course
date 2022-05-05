global string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    print('---> Browser opened')
    browser = webdriver.Chrome()
    yield browser
    print("---> Browser closed")
    browser.quit()


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


class Testing():
    @pytest.mark.parametrize('link', links)
    def test_stepik(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(7)
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        x = math.log(int(time.time()))
        textarea.send_keys(x)
        btn = browser.find_element(By.XPATH, "//div/button[@class ='submit-submission' ]").click()
        time.sleep(1)
        string = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        list = []
        if string.text != "Correct!":
            list.append(string.text)

    print(list)
