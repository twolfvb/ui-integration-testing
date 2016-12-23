import os
import time
import unittest

from selenium.webdriver import ActionChains

from drivers.chrome import get_driver

class TestDnD(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()

        # Navigate to DarwinEd
        self.driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
        time.sleep(5)

    def test(self):
        driver = self.driver

        action_chains = ActionChains(driver)

        source = self.driver.find_element_by_id('draggable')
        target = self.driver.find_element_by_id('droppable')

        action_chains.drag_and_drop(source, target).perform()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
