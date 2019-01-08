class LoginPage(object):
    CHOOSE_EMAIL_AUTH_BUTTON = 'com.todoist:id/btn_welcome_continue_with_email'
    EMAIL_FIELD = 'com.todoist:id/email_exists_input'
    CONTINUE_WITH_EMAIL_BUTTON = 'com.todoist:id/btn_continue_with_email'
    PASSWORD_FIELD = 'com.todoist:id/log_in_password'
    LOGIN_BUTTON = 'com.todoist:id/btn_log_in'

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(5)

    def choose_email_auth(self):
        self.driver.find_element_by_id(self.CHOOSE_EMAIL_AUTH_BUTTON).click()

    def type_email(self, email):
        self.driver.find_element_by_id(self.EMAIL_FIELD).send_keys(email)

    def continue_with_email(self):
        self.driver.find_element_by_id(self.CONTINUE_WITH_EMAIL_BUTTON).click()

    def type_password(self, password):
        self.driver.find_element_by_id(self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.choose_email_auth()
        self.type_email(email)
        self.continue_with_email()
        self.type_password(password)
        self.click_login_button()
