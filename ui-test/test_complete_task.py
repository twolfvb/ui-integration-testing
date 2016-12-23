import time

import unittest
import uuid

from drivers.chrome import get_driver

from pages import ListPage, AddTaskPage
from router import Router

class TestCompleteTaskCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(10) # seconds
        self.router = Router()

    def testAddTask(self):
        driver = self.driver
        router = self.router

        # initial page
        main_page = ListPage(driver)

        todo_id = str(uuid.uuid4())
        self._create_todo(todo_id)
        print('first', todo_id)

        # reload main page
        router.browse_to(driver, main_page)
        # wait a bit
        time.sleep(1)

        # complete task
        print('reorder')
        main_page.complete_task(todo_id)

        # wait
        time.sleep(5)

    def _create_todo(self, todo_id):
        driver = self.driver
        router = self.router

        # initial page
        main_page = ListPage(driver)

        # browse to page
        router.browse_to(driver, main_page)

        # follow link to add task
        main_page.follow_to_add_task()

        # now we are in add task page
        add_task_page = AddTaskPage(driver)

        # add a todo (redirects back to list on success)
        add_task_page.add(
            todo_id,
            is_completed=False,
            is_favorite=True
        )

        # check
        self.assertTrue(main_page.task_exists(todo_id))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
