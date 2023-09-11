from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path='resourse/chromedriver/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = "https://www.toolsqa.com/selenium-training/"
driver.get(url)
header = driver.execute_script("return document.head.innerHTML")
print(header)
driver.quit()
