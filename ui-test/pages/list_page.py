from selenium.webdriver import ActionChains

from page import Page

from list_page_locators import ListPageLocators

class ListPage(Page):
    route = '/'

    def follow_to_add_task(self):
        el = self.driver.find_element(*ListPageLocators.ADD_TASK_BUTTON)
        el.click()

        return 'add_task'

    def task_exists(self, todo_id):
        return todo_id in self.driver.page_source

    def complete_task(self, todo_id):
        finder = ListPageLocators.complete_task_button(todo_id)
        complete_button  = self.driver.find_element(*finder)
        complete_button.click()

    def reorder_tasks(self):
        source_element = self.driver.find_element(*ListPageLocators.FIRST_TASK_LI)
        dest_element = self.driver.find_element(*ListPageLocators.LAST_TASK_LI)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element)
        actions.move_to_element(dest_element)
        actions.release(source_element)
        actions.perform()

    def filter_all(self):
        pass

    def filter_pending(self):
        pass

    def filter_completed(self):
        pass
