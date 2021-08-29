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
  
   
login("http://10.39.234.54/centreon/", "useralias", "dt_supervision", "password", "DT2020$", "submitLogin")
#Service Data counter
urls=["http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;CAPS",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;sw_check_diameter_data_counters",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;sw_check_diameter_open_data_sessions",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;sw_check_diameter_activesess",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;sw_check_diameter_calls_active",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsmngt.djiboutitelecom.dj;Memory_Usage",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;Memory_Usage",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;Interface_eth0",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;Interface_eth1",
      "http://10.39.234.54/centreon/main.php?p=204&mode=0&svc_id=ocsstd.djiboutitelecom.dj;Interface_eth2"
     
      ]
ids=[ "#graph_wrapper_100_312 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_327 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_329 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_324 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_325 > div.title > a:nth-child(4)",
      "#graph_wrapper_99_227 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_279 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_265 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_266 > div.title > a:nth-child(4)",
      "#graph_wrapper_100_267 > div.title > a:nth-child(4)"   
   ]
x=0
for i in urls:
   mystring = str(x)
   mystring = "screen/"+mystring+".png"
   clicked(i,mystring,ids[x])
   x=x+1
  

  # Opens a image in RGB mode 

 