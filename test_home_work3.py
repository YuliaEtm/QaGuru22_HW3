import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.window_width = 800
    browser.config.window_height = 600

    browser.open('https://ya.ru/')
    yield
    browser.quit()


def test_search_positive(browser_settings):

    browser.element('[id="text"]').should(be.blank).type('ga.guru').press_enter()
    browser.element('html').should(have.text('Курсы тестировщиков'))


def test_search_found_nothing(browser_settings):

    browser.element('[id="text"]').should(be.blank).type('asasasassadfgg').press_enter()
    browser.element('[class = "EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))
