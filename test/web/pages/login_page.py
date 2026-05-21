from playwright.sync_api import Page
from web.pages.page_base import PageBase  
class LoginPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password":  "#password",
            "btn_login": "#login",
            "btn_register": "#register"
        })

    def login(self, username, password):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("btn_login").click()

    def go_to_register(self):
        self.element("btn_register").click()