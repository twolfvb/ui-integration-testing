import time

import unittest
import uuid

from drivers.chrome import get_driver

from pages import ListPage, AddTaskPage
from router import Router

class TestReorderTasksCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(10) # seconds
        self.router = Router()

    def testAddTask(self):
        driver = self.driver
        router = self.router

        # initial page
        main_page = ListPage(driver)

        todo_a_id = str(uuid.uuid4())
        todo_b_id = str(uuid.uuid4())
        print('first', todo_a_id)
        print('last', todo_b_id)

        self._create_todo(todo_a_id)
        self._create_todo(todo_b_id)

        # reload main page
        router.browse_to(driver, main_page)
        # wait a bit
        time.sleep(2)

        # reorder tasks
        print('reorder')
        main_page.reorder_tasks()

        # wait
        time.sleep(3)

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
