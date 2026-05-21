import uuid
import pytest
import requests
from playwright.sync_api import expect
from web.test_base import WebBase
from web.pages.login_page import LoginPage
from web.pages.register_page import RegisterPage
from web.pages.calculator_page import CalculatorPage

class TestWeb(WebBase):
    
    def setup_method(self):
        try:
            requests.post("http://localhost:5000/logout")
        except Exception:
            pass

        super().setup_method()
        self.unique_user = f"testuser_{uuid.uuid4().hex[:8]}"
        self.password = "Pass123!"
        
        self.login_page = LoginPage(self.page)
        self.register_page = RegisterPage(self.page)
        self.calc_page = CalculatorPage(self.page)

    def _register_and_login_helper(self):
        self.login_page.go_to_register()
        self.register_page.register_user(self.unique_user, self.password)
        self.calc_page.verify_user_logged_in(self.unique_user)

    def test_register_new_user(self):
        self._register_and_login_helper()

    def test_calculation_methods(self):
        self._register_and_login_helper()
        
        self.calc_page.calculate(3, 2, "+")
        expect(self.calc_page.element("screen")).to_have_value("5")
        
        self.calc_page.calculate(9, 4, "-")
        expect(self.calc_page.element("screen")).to_have_value("5")
        
        self.calc_page.calculate(4, 2, "*")
        expect(self.calc_page.element("screen")).to_have_value("8")
        
        self.calc_page.calculate(8, 2, "/")
        expect(self.calc_page.element("screen")).to_have_value("4")

    def test_history_feature(self):
        self._register_and_login_helper()
        
        self.calc_page.calculate(5, 4, "+")
        
        self.calc_page.toggle_history()
        
        history_text = self.calc_page.get_history()
        assert "=9" in history_text