from src.dao.LoginPageDAO import LoginPageDAO

class LoginScenario:
    def __init__(self, page):
        self.login_dao = LoginPageDAO(page)

    def login_with_valid_credentials(self, username, password):
        self.login_dao.login_with_valid_credentials(username, password)

        return self.login_dao.get_swaglabs_text()


    def login_with_invalid_credentials(self, username, password):
        self.login_dao.login_with_invalid_credentials(username, password)

        return self.login_dao.get_swaglabs_text()