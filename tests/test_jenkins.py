import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from utils import attach


def test_azalia_decorator_steps():
    open_main_page("https://azalianow.ru/")
    close_advertising()
    search_flower("Хризантема")
    check_result("Хризантема")


@allure.step("Открываем главную страницу")
def open_main_page(mainpage):
    browser.open(mainpage)


@allure.step("Закрываем рекламу")
def close_advertising():
    s("[class^='MobileAppAdvertModal_modalCloseBtn']").click()


@allure.step("Ищем в поиске цветок {flower}")
def search_flower(flower):
    s("[inputmode=search]").send_keys(flower).press_enter()


@allure.step("Проверяем наличие текста хризантема в результатах поиска")
def check_result(flower):
    s(by.partial_text(flower)).should(be.visible)

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)