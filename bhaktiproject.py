import selenium 

import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://twitter.com/i/flow/login') 

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("KharateBhakti")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

#password
sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('24092001')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

sleep(6)
Tweet = driver.find_element_class_name(By.XPATH,".//div[@data-testid='tweetText']").text
Tweet2 = Tweet+"Neutral"
print(Tweet2)
#driver.execute_script("arguments[0].textContent= '{Tweet2}'", Tweet)
#driver.execute_script("document.querySelector('.data-testid='tweetText'').textContent = '{Tweet2}'".format(Tweet2))
#driver.execute_script("arguments[0].textContent = f'{Tweet2} 'Hello, world!'", Tweet)
driver.execute_script("var element = document.querySelector('.css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'); element.textContent += ' Neurtal';")
