import logging
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Standard timeout (in seconds) to wait for a page element to appear.
TIMEOUT = 5

class TestLoginformtest():
  def __init__(self, base_url):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(TIMEOUT)
    self._base_url = base_url

  def get(self, relative_url):
    full_url = self._base_url + relative_url
    logging.info('Loading url: %s', full_url)
    self.driver.get(full_url)
  
  def test_loginformtest(self):
    logging.info('Navigating to page')
    self.get("/styled/basic-html-form-test.html")
    logging.info('Clicking on "username" textbox')
    self.driver.find_element(By.NAME, "username").click()
    logging.info('Filling in textbox with "test"')
    self.driver.find_element(By.NAME, "username").send_keys("test")
    logging.info('Clicking on "password" textbox')
    self.driver.find_element(By.NAME, "password").click()
    logging.info('Filling in textbox with "test"')
    self.driver.find_element(By.NAME, "password").send_keys("test")
    logging.info('Clicking on "commentsd" textbox')
    self.driver.find_element(By.NAME, "comments").click()
    logging.info('Filling in textbox with "Commtstents..."')
    self.driver.find_element(By.NAME, "comments").send_keys("Commtstents...")
    logging.info('Selecting radio button 2')
    self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='rd2']").click()
    logging.info('Choosing Drop Down Item 2')
    dropdown = Select(self.driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_visible_text('Drop Down Item 2')
    logging.info('Clicking "submit"')
    self.driver.find_element(By.CSS_SELECTOR, ".styled-click-button:nth-child(2)").click()

  def quit(self):
    logging.info('Exiting test driver')
    self.driver.quit()

def main(args):
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info('Starting script')
    driver = TestLoginformtest(args.url)
    driver.test_loginformtest()

    driver.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    main(parser.parse_args())
