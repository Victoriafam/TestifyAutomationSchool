# Setup your IDE
# Print "hello world" into the console
# Print your name in the console

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


print("Hello World")

name = "Victoria"
print("My name is " + name)