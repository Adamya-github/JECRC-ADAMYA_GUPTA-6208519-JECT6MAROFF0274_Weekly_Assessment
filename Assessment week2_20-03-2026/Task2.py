from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)
driver.get("https://automationexercise.com/signup")
driver.maximize_window()
sleep(2)

driver.find_element(By.NAME, "name").send_keys("ngs")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("i123@gmail.com")
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
sleep(2)

wait.until(EC.presence_of_element_located((By.ID, "id_gender1")))
driver.find_element(By.ID, "id_gender1").click()
newsletter = driver.find_element(By.NAME, "newsletter")
offers = driver.find_element(By.NAME, "optin")
newsletter.click()
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Offers selected:", offers.get_attribute("checked"))

driver.quit()