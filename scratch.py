import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(20)
driver.get("https://internshala.com/registration/student")
link=driver.find_element_by_xpath("//span[@data-target='#login-modal']")
link.click()
username=driver.find_element_by_xpath("//input[@name='email']")
username.send_keys("")#Email
password=driver.find_element_by_xpath("//input[@id='modal_password']")
password.send_keys("")#password
submit=driver.find_element_by_xpath("//button[@id='modal_login_submit']")
submit.click()

element1=driver.find_element_by_link_text("Computer Science Internship")
element1.click()
try:
  soni=driver.find_elements_by_class_name('matching_preference_container form-group checkbox')
  for sdf in soni:
    prefe3=sdf.find_element_by_xpath("//input[@id='matching_preference_mobile']")
    prefe3.click()
    prefe3.click()
    prefe3.click()

except:
    print('error4')



#elems = driver.find_elements_by_xpath("//a[@href]")
#for elem in elems:
    #a=elem.get_attribute("href")
    #print(a)
try:
    place=driver.find_elements_by_xpath("//input[@placeholder='Enter text ...']")
    for i in place:
      i.send_keys("It is in my github profile")
except:
     pass
try:
    place=driver.find_elements_by_xpath("//textarea[@placeholder='Enter text ...']")
    for zxc in place:
      zxc.send_keys("It is in my github profile")
except:
     pass


