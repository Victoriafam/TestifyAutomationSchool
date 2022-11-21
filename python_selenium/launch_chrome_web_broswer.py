from selenium import webdriver
import  chromedriver_autoinstaller
def main():
    chromedriver_autoinstaller()
    driver = webdriver.chrome()
    driver.get("http://www.google/org")
    driver.close()





main(
    

