import os 
from selenium import webdriver
import time
from PIL import Image 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("file:///C:/Users/Abdifatah/Desktop/New%20Folder/HC_AAA_PRD-3A-APP-01_20210826083001.log")
time.sleep(2)
driver.save_screenshot("screenhc/0.png")
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(2)
driver.save_screenshot("screenhc/1.png")
driver.execute_script("window.scrollTo(0, 1800)")
time.sleep(2)
driver.save_screenshot("screenhc/2.png")

driver.close()

im = Image.open(r"screenhc/0.png") 
width, height = im.size
print(width, height) 
left = 0
top = 0
right = 700
bottom = 300
im1 = im.crop((left, top, right, bottom)) 
im1.save(r"Capture.png") 



im = Image.open(r"screenhc/0.png") 
width, height = im.size
print(width, height)
left = 0
top = height / 3
right = 900
bottom = 500
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture1.png") 


im = Image.open(r"screenhc/1.png") 
width, height = im.size
print(width, height)
left = 0
top = height / 2
right = 1100
bottom = 650
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture2.png") 
 

im = Image.open(r"screenhc/2.png") 
width, height = im.size
print(width, height)
left = 0
top = 0
right = 1100
bottom = 450
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture3.png") 


im = Image.open(r"screenhc/3.png") 
width, height = im.size
print(width, height)
left = 0
top = height / 5
right = 1100
bottom = 630
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture4.png") 


im = Image.open(r"screenhc/4.png") 
width, height = im.size
print(width, height)
left = 0
top = height / 4
right = 1100
bottom = 500
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture4.png") 


im = Image.open(r"screenhc/4.png") 
width, height = im.size
print(width, height)
left = 0
top = height / 2
right = 1500
bottom = 900
im1 = im.crop((left, top, right, bottom))  
im1.save(r"Capture4.png") 








