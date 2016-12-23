from selenium.webdriver.common.by import By

class AddTaskPageLocators(object):
    DESCRIPTION_INPUT = (By.NAME, 'description')
    IS_COMPLETED_INPUT = (By.NAME, 'is_completed')
    IS_FAVORITE_INPUT = (By.NAME, 'is_favorite')
