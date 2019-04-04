from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote('http://chrome:4444', DesiredCapabilities.CHROME)
driver.get('https://boulder.craigslist.org/');
driver.save_screenshot('screenshots/example.png');