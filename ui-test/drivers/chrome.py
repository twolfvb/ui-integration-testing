from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_driver():
    chromedriver = '/home/jonathan/bin/chromedriver'

    # Set options for chrome
    prefs = {
        'download.default_directory': '/tmp'
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)

   # Instantiate driver
    driver = webdriver.Chrome(
        executable_path=chromedriver,
        chrome_options=chrome_options
    )

    return driver
