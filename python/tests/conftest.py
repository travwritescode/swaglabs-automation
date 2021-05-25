"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from pages.login import SwagLabsLoginPage
from pathlib import Path


@pytest.fixture
def config(scope='session'):

    # Read the file
    p = Path('./python/config.json').resolve()
    with open(p) as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]} is not supported')

    # Makes its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()


@pytest.fixture()
def login_user(browser):

    login_page = SwagLabsLoginPage(browser)

    # Log in user for test
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
