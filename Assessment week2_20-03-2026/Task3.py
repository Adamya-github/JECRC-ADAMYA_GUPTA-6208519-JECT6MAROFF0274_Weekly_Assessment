from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)

search = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='gLFyf']")))
search.send_keys("Selenium Python")

suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for s in suggestions:
    print(s.text)

suggestions[0].click()
sleep(20)
driver.quit()