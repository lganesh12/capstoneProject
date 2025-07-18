<<<<<<< HEAD
from features.locators import locator


class Login:
    def __init__(self,page):
        self.page = page

    def enter_username(self,username):
        self.page.locator([locator("username_text_box")]).fille(username)
    def enter_password(self,password):
        self.page.locator([locator("password_text_box")]).fille(password)
    def click_login(self):
        self.page.locator([locator("login_button")]).click()
    def login(self,username,password):
        self.enter_password(username)
        self.enter_password(password)
        self.click_login()
    def is_user_logged_in(self):
        return self.page.title() == "Swag Labs"
=======
from features.locators import dict_locators


class Login:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        breakpoint()
        self.page.locator("//input[@id='user-name']").fill(username)

    def enter_password(self, password):
        self.page.locator("//input[@id='password']").fill(password)

    def click_login(self):
        self.page.locator("//input[@id='login-button']").click()

    def login(self, username, password):
        self.enter_password(username)
        self.enter_password(password)
        self.click_login()

    def is_user_logged_in(self):
        return self.page.title() == "Swag Labs"
>>>>>>> ef4417a (Added files)
