from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.marketwatch.com/investing/stock/aapl"
driver.get(url)

time.sleep(5)  

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

key_data_section = soup.find('body')
print(key_data_section)