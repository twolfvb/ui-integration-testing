from selenium.webdriver.support import expected_conditions as EC

from page import Page

from add_task_page_locators import AddTaskPageLocators

class AddTaskPage(Page):
    route = '/add_task'

    def add(self, description, is_completed=False, is_favorite=False):
        # type description
        el = self.driver.find_element(*AddTaskPageLocators.DESCRIPTION_INPUT)
        el.send_keys(description)

        # check is_completed
        el = self.driver.find_element(*AddTaskPageLocators.IS_COMPLETED_INPUT)
        if is_completed:
            el.click()

        # check is_favorite
        el = self.driver.find_element(*AddTaskPageLocators.IS_FAVORITE_INPUT)
        if is_favorite:
            el.click()

        import time; time.sleep(3)

        # submit form
        el.submit()

        # wait for form
        import time; time.sleep(1)

        return 'list'

    def cancel(self):
        return 'list'
