from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '$'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}

BASE_URL = "http://www.amazon.com/"

msedgedriver = "./msedgedriver.exe"

options = EdgeOptions()
#driver = webdriver.Edge(executable_path = msedgedriver)

def get_web_driver(options):
    return Edge(executable_path = msedgedriver, options = options)

def get_web_driver_options():
    return options

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')