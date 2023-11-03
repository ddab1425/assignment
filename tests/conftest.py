import undetected_chromedriver as uc
import pytest

@pytest.fixture(scope="session")
def launch_chrome_driver():
    options = uc.ChromeOptions()
    options.headless = False
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()
