import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()


class TestRegistration_numberInput:
    def test_reg_validNumber(self):
        driver.get('https://www.ozon.ru/')
        driver.maximize_window()
        log_in = driver.find_element(By.CLASS_NAME, 'ba3i').click() #Нажимаю на кнопку входа
        driver.implicitly_wait(10) #Ожидание прогрузки iframe
        iframe = driver.find_element(By.ID, 'authFrame') #Находим iframe
        driver.switch_to.frame(iframe) #Переключаемся на работу в фрейме
        phone = driver.find_element(By.XPATH, "//input[@class = 'ui-h5 ui-h9']") #Находим инпут ввода номера
        phone.send_keys('9961282759')
        driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click() # Нажимаем "Войти"
        time.sleep(2)
        assert user_is_authorised(), "User is guest"
        driver.quit()
    def test_reg_emptyNumber(self):
        driver.get('https://www.ozon.ru/')
        driver.maximize_window()
        log_in = driver.find_element(By.CLASS_NAME, 'ba3i').click()
        driver.implicitly_wait(10)
        iframe = driver.find_element(By.ID, 'authFrame')
        driver.switch_to.frame(iframe)
        phone = driver.find_element(By.XPATH, "//input[@class = 'ui-h5 ui-h9']")
        phone.send_keys('')
        driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
        n = driver.find_element(By.CSS_SELECTOR, "[class = 'ui-s1']") # Находим элемент с тектом ошибки
        text = n.text
        error = WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class = 'ui-s1']"), "Заполните телефон"))
        #Ждем состояния,когдаона появиться
        print('Ошибка отсутсвия введеного номера появляется') # При появлении - печатаем сообщение
        driver.quit()


