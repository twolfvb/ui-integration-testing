import time

import unittest
import uuid

from drivers.firefox import get_driver

from pages import ListPage, AddTaskPage
from router import Router

class AddTaskCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(10) # seconds
        self.router = Router()

    def testAddTask(self):
        driver = self.driver
        router = self.router

        # initial page
        main_page = ListPage(driver)

        # browse to page
        router.browse_to(driver, main_page)

        # time.sleep(3)

        # follow link to add task
        main_page.follow_to_add_task()

        # time.sleep(3)

        # now we are in add task page
        add_task_page = AddTaskPage(driver)

        # add a todo (redirects back to list on success)
        todo_id = str(uuid.uuid4())
        add_task_page.add(
            todo_id,
            is_completed=False,
            is_favorite=True
        )

        # time.sleep(3)

        # check
        self.assertTrue(main_page.task_exists(todo_id))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
