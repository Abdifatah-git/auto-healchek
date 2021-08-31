import os 
from selenium import webdriver
from PIL import Image 
import time

def clicked(url,screen,id):
   time.sleep( 1 )
   driver.get(url)
   button = driver.find_element_by_css_selector(id)
   time.sleep( 1 )
   button.click()
   driver.execute_script("document.body.style.zoom='64%'")
   time.sleep( 2 )
   driver.execute_script("window.scrollTo(1080, 0)")
   time.sleep(2)
   driver.save_screenshot(screen)
   print(url)
   print(screen)
  
 

driver = webdriver.Chrome()
driver.maximize_window()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_name(usernameId).send_keys(username)
   driver.find_element_by_name(passwordId).send_keys(password)
   driver.find_element_by_name(submit_buttonId).click()
  
   
login("url", "usernameId", "username", " passwordId", "password", "submit_buttonId")
#Service Data counter
urls=[
     
      ]
ids=[
   ]
x=0
for i in urls:
   mystring = str(x)
   mystring = "screen/"+mystring+".png"
   clicked(i,mystring,ids[x])
   x=x+1
  
 
