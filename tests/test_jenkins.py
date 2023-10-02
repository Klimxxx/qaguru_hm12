import os
import allure
from selene import have, command, browser
from selene.support.shared import browser

from selene.support.conditions import be


@allure.step("Успешная регистрация")
def test_open_page_remove_ad():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')

    # browser.execute_script("$('#adplus-anchor'). remove ()")
    # browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Вводим данные"):
        browser.element('[id=firstName]').should(be.blank).type('Elena')
        browser.element('[id=lastName]').should(be.blank).type('Pirogova')
        browser.element('[id=userEmail]').should(be.blank).type('123@123.ru')
        browser.element('[id^=gender-radio][value=Female]+label').click()
        browser.element('[id=userNumber]').should(be.blank).type('8987654321')
        browser.element('#dateOfBirthInput').click()
        browser.element('select[class^=react-datepicker__year]').send_keys('1989')
        browser.element('.react-datepicker__month-select').send_keys('January')
        browser.element('[aria-label= "Choose Monday, January 2nd, 1989"]').click()
        browser.element('#subjectsInput').send_keys('English')
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('English')).click()
        browser.element('[id="hobbies-checkbox-2"]+label').perform(command.js.scroll_into_view).click()
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'resources/image.png')))
        browser.element('[id=currentAddress]').should(be.blank).type('Kazakhstan')
        browser.element('#state').perform(command.js.scroll_into_view).click().all(
            '[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#city').click()
        browser.element('[id="react-select-4-option-0"]').click()
        browser.driver.set_window_size(400, 1000)
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    # with allure.step("Проверяем результат"):
        browser.element('.table').all('td').should(have.texts(
                'Student Name', 'Elena Pirogova',
                'Student Email', '123@123.ru',
                'Gender', 'Female',
                'Mobile', '8987654321',
                'Date of Birth', '2 January,1989',
                'Subjects', 'English',
                'Hobbies', 'Reading',
                'Picture', 'image.png',
                'Address', 'Kazakhstan',
                'State and City', 'NCR Delhi'
            ))


# @allure.step("Проверяем наличие текста хризантема в результатах поиска")
# def check_result(flower):
#     s(by.partial_text(flower)).should(be.visible)
#
#     attach.add_html(browser)
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)