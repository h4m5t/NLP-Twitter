#测试webdriver功能
from selenium import webdriver
import time

driverOptions = webdriver.ChromeOptions()
# r代表后面的字符串斜杠不转义，''表示python识别空格
driverOptions.add_argument(r"user-data-dir=C:\Users\loeoe\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(executable_path=r"E:\\Temp\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe",port=0,chrome_options=driverOptions)

driver.get("https://www.google.com")