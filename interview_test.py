import os
import time
import unittest
from appium import webdriver
from api import TodoistService
from api.TodoistService import *
from mobile.pages.LoginPage import LoginPage
from mobile.pages.HomePage import HomePage
from .config import email, password


class InterviewSuite(unittest.TestCase):

    testProject = 'Interview'
    task = 'Make a project using Java?'

    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.0',
                        'deviceName': 'Android Emulator',
                        'automationName': 'UiAutomator2',
                        'app': os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                            'app/Todoist_v12.8_apkpure.com.apk')),
                        'appPackage': 'com.todoist',
                        'appActivity': '.activity.HomeActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.mobile_assert_poll_timeout = 2
        self.mobile_assert_retries = 3

    def tearDown(self):
        self.driver.quit()
        delete_task(self.task)

    @classmethod
    def tearDownClass(cls):
        delete_project(cls.testProject)

    def test_create_project(self):

        add_project(self.testProject)

        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        home_page = HomePage(self.driver)

        assert self.testProject in home_page.list_projects()

    def test_create_task_via_mobile(self):

        task_count = len(TodoistService.find_task(self.task))

        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        home_page = HomePage(self.driver)
        home_page.switch_project(self.testProject)
        home_page.create_task(self.task)

        # A simple poller for the asynchronous mobile action (task create)
        for i in range(self.mobile_assert_retries):
            if len(TodoistService.find_task(self.task)) == task_count + 1:
                break
            else:
                time.sleep(self.mobile_assert_poll_timeout)

        # Assert seems rather gimmicky after the poller...
        assert (task_count + 1) == len(TodoistService.find_task(self.task))

    def test_reopen_task(self):
        task_count = len(TodoistService.find_task(self.task))

        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        home_page = HomePage(self.driver)
        home_page.switch_project(self.testProject)
        home_page.create_task(self.task)
        home_page.complete_task(self.task)
        for i in range(self.mobile_assert_retries):
            tasks = TodoistService.find_task(self.task)
            if len(tasks) == task_count + 1 and tasks[-1].data.get('checked') == 1:
                TodoistService.reopen_task_by_id(tasks[-1].data.get('id'))
                break
            else:
                time.sleep(self.mobile_assert_poll_timeout)
        home_page.refresh()
        assert self.task in home_page.list_tasks()
