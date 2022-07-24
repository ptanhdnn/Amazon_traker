from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

driver = webdriver.Edge(executable_path = "./msedgedriver.exe")
driver2 = Edge(executable_path = "./msedgedriver.exe")
driver2.get("http://google.com")