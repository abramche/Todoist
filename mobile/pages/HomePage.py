from appium.webdriver.common.touch_action import TouchAction


class HomePage(object):
    MAIN_PROJECT_SCREEN = 'android:id/content'
    ITEMS = 'com.todoist:id/text'
    COMPLETE_TASK = 'com.todoist:id/menu_item_complete'
    CREATE_TASK = 'com.todoist:id/fab'
    TASK_INPUT_FIELD = 'android:id/message'
    CHANGE_VIEW_BUTTON = 'Change the current view'
    EXPAND_PROJECT_LIST = '//android.widget.ImageView[@content-desc="Expand/collapse"][1]'
    CREATE_PROJECT = '//android.widget.ImageButton[@content-desc="Add"])[1]'
    PROJECT_LIST = '//android.widget.RelativeLayout[@resource-id="android:id/content"]' \
                   '/android.widget.TextView[@resource-id="com.todoist:id/name"]'
    PROJECT_NAME_INPUT = 'com.todoist:id/name'

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(5)

    def create_task(self, content):
        self.driver.find_element_by_id(self.CREATE_TASK).click()
        self.driver.find_element_by_id(self.TASK_INPUT_FIELD).send_keys(content)
        self.driver.press_keycode(66)  # Enter
        self.driver.press_keycode(111)  # Escape - to close the keyboard popup

    def complete_task(self, name):
        assert name in self.list_tasks()
        for task in self.driver.find_elements_by_id(self.ITEMS):
            if task.text == name:
                task.click()
        self.driver.find_element_by_id(self.COMPLETE_TASK).click()

    def click_task(self, name):
        assert name in self.list_tasks()
        for task in self.driver.find_elements_by_id(self.ITEMS):
            if task.text == name:
                task.click()

    def open_sidebar(self):
        self.driver.find_element_by_accessibility_id(self.CHANGE_VIEW_BUTTON).click()

    def expand_project_list(self):
        self.driver.find_element_by_xpath(self.EXPAND_PROJECT_LIST).click()

    def click_create_project(self):
        self.driver.find_element_by_xpath(self.CREATE_PROJECT).click()

    def type_new_project_name(self, name):
        self.driver.find_element_by_id(self.PROJECT_NAME_INPUT).send_keys(name)
        self.driver.press_keycode(66)

    def switch_project(self, name):
        assert name in self.list_projects(), \
            "%s is not in the available projects: %s" % (name, str(self.list_projects()))
        for project in self.driver.find_elements_by_xpath(self.PROJECT_LIST):
            if project.text == name:
                project.click()

    def list_projects(self):
        self.open_sidebar()
        self.expand_project_list()
        projects = []
        for element in self.driver.find_elements_by_xpath(self.PROJECT_LIST):
            projects.append(element.text)
        return projects

    def list_tasks(self):
        tasks = []
        for task in self.driver.find_elements_by_id(self.ITEMS):
            tasks.append(task.text)
        return tasks

    def refresh(self):
        screen_size = self.driver.get_window_size()
        screen_width = screen_size.get('width')
        screen_height = screen_size.get('height')
        element = self.driver.find_element_by_id(self.MAIN_PROJECT_SCREEN)
        actions = TouchAction(self.driver)
        actions.press(element, int(screen_width / 2), int(screen_height * 0.2))\
            .wait(500)\
            .move_to(element, int(screen_width / 2), int(screen_height * 0.8))\
            .release()\
            .perform()
