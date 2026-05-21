from playwright.sync_api import Page
from web.pages.page_base import PageBase  
class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password_1": "#password1",
            "password_2": "#password2",
            "btn_register": "button#register"
        })

    def register_user(self, username, password):
        self.element("username").fill(username)
        self.element("password_1").fill(password)
        self.element("password_2").fill(password)
        self.element("btn_register").click()