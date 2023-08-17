from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.set_window_size(600, 800)
driver.get('https://www.cathaybk.com.tw/cathaybk/')
wait = WebDriverWait(driver, 10)
driver.save_screenshot('autotest/screenshot1.png')
driver.quit()
