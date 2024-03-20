from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
url = 'https://wise.com/gb/currency-converter/usd-to-brl-rate?amount=50'
driver.get(url)
result = driver.find_element(By.XPATH, '//*[@id="target-input"]')
print(result.get_attribute('value'))
driver.close()
