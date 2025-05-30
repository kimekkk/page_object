from pages.main_page import MainPage
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page()          

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
    page.open()
    page.go_to_basket()
    BasketPage(browser, browser.current_url).should_be_empty_basket()


