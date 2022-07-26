from lib2to3.pgen2 import driver
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

base_url = "http://www.amazon.com/"

def get_web_driver(options):
    return Edge(executable_path = "./msedgedriver.exe", options = options)

def get_web_driver_options():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('start-maximized')
    options.add_argument("--disable-extensions")
    return options

def get_link(driver, base_url):
    driver.get(base_url)

#driver2 = Edge(executable_path = "./msedgedriver.exe")
options = get_web_driver_options() 
driver = get_web_driver(options)
get_link(driver, base_url)
driver.quit()

#driver.quit()