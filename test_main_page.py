from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_for_login_or_reg(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_quest_should_see_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_quest_should_see_registration_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()