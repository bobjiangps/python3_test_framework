from .common_component import CommonComponent


class LoginPage(CommonComponent):

    def login(self, account, pwd):
        self.log.info("Start to login with account: %s and password: %s" % (str(account), str(pwd)))
        if self.element("login_link").element_exist():
            self.go_to_login_page()
            self.element("account_input").input_value(account)
            self.element("password_input").input_value(pwd)
            self.element("login_button").click()
            self.element("logout_link").wait_presence()
            self.log.info("Complete to login")
        else:
            self.log.info("Already logged in")
