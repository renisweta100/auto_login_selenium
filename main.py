from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://the-internet.herokuapp.com/login")

check = driver.find_element(By.ID, "username")
check.clear()
check.send_keys("tomsmith")
pass_input = driver.find_element(By.ID, "password")
pass_input.clear()
pass_input.send_keys("SuperSecretPassword!" +Keys.ENTER)



try:
    element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flash"))
    )
    message = element.text
    print(message)

except:


    driver.quit()


