from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = opts)
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)
print("Website opened successfully")

# 1. Locate the username field using CSS Selector with Tag and name attribute.
username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print(username)
print("Username field found")

# 2. Locate the password field using CSS Selector with Tag and id attribute.
password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
print(password)
print("Password field found")

# 3. Locate the "Login" button using CSS Selector with Tag and type attribute.
login_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print(login_btn)
print("Login button found")

# 4. Locate the footer link ("Elemental Selenium") using CSS Selector(descendant).
footer_link = driver.find_element(By.CSS_SELECTOR,'div[style = "text-align: center;"] a')
print(footer_link)
print("Elemental Selenium link found")

sleep(3)

driver.quit()