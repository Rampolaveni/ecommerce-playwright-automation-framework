from src.commonUtility.CommonActions import CommonActions
from src.objectRepository.LoginPageObjects import LoginPageObjects

class LoginPageDAO:
    def __init__(self, page):
        self.actions = CommonActions(page)


    def enter_username(self, username):
        self.actions.send_keys(LoginPageObjects.USERNAME, username)

    def enter_password(self, password):
        self.actions.send_keys(LoginPageObjects.PASSWORD, password)

    def click_login(self):
        self.actions.click(LoginPageObjects.LOGIN_BUTTON)

    def login_with_valid_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def login_with_invalid_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_swaglabs_text(self):
        return self.actions.get_text(LoginPageObjects.SWAG_LABS)
