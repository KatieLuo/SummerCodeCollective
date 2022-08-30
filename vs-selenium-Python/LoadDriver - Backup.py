
#to open chrome driver
from selenium import webdriver
website='https://www.facebook.com'
path = '/Users/luoka/OneDrive/Documents/SummerCodeLab/chromedriver'


driver=webdriver.Chrome(path)
driver.get(website)
#driver.quit()

