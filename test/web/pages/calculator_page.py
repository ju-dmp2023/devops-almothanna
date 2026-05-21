from playwright.sync_api import Page, expect
from web.pages.page_base import PageBase  
class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "screen": "#calculator-screen",
            "history": "#history",
            "btn_toggle": "#toggle-button",
            "lbl_username": "#user-name",
            "btn_add": "#key-add",
            "btn_sub": "#key-subtract",
            "btn_mul": "#key-multiply",
            "btn_div": "#key-divide",
            "btn_eq": "#key-equals"
        })

    def click_number(self, num: int):
        self.page.locator(f"#key-{num}").click()

    def calculate(self, a: int, b: int, operation: str):
        self.click_number(a)
        
        if operation == "+":
            self.element("btn_add").click()
        elif operation == "-":
            self.element("btn_sub").click()
        elif operation == "*":
            self.element("btn_mul").click()
        elif operation == "/":
            self.element("btn_div").click()
            
        self.click_number(b)
        self.element("btn_eq").click()

    def get_screen_value(self):
        return self.element("screen").input_value()

    def toggle_history(self):
        self.element("btn_toggle").click()

    def get_history(self):
        return self.element("history").input_value()

    def verify_user_logged_in(self, expected_username):
        expect(self.element("lbl_username")).to_contain_text(expected_username)