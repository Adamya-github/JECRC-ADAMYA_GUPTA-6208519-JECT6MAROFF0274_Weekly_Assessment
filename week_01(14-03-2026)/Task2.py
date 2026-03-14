from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = opts)

# 1. Navigate to Wikipedia
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
sleep(2)
print("Wikipedia opened successfully")

# 2. Find search input field
search = driver.find_element(By.ID, "searchInput")
print(search)
print("Search input field found")

# 3. Find English language
english = driver.find_element(By.ID, "js-link-box-en")
print(english)
print("English language link found")

# 4. Find main Wikipedia logo image
logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print(logo)
print("Wikipedia logo found")

# 5. Count language links in central block
languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured a")
print(languages)
print(len(languages))
print("Total language links found")
sleep(2)

# 6. Navigate back
driver.back()
print("Navigated back")
sleep(2)

# 7. Navigate forward
driver.forward()
print("Navigated forward")
sleep(2)

# 8. Refresh page
driver.refresh()
print("Page refreshed")
sleep(2)

# 9. Print final page title
print("Final Page Title:", driver.title)

# 10. Quit browser
driver.quit()