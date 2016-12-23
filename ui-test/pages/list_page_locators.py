from selenium.webdriver.common.by import By

class ListPageLocators(object):
    ADD_TASK_BUTTON = (By.LINK_TEXT, 'Add Task')
    FIRST_TASK_LI = (By.CSS_SELECTOR, '#items li:first-child')
    LAST_TASK_LI = (By.CSS_SELECTOR, '#items li:last-child')
    BUTTON_PATH = """//*[@id="items"]/li[contains(text(), '{}')]/form[1]/button"""

    @classmethod
    def complete_task_button(cls, todo_id):
        path = cls.BUTTON_PATH.format(todo_id)
        return (By.XPATH, path)
