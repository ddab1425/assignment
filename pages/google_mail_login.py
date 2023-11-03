from selenium.webdriver.common.by import By
from placementsio.base.base_page import BasePage
from placementsio.data.google_mail_inbox_data import TestMailAccount

class GoogleMailLoginPageLocators:
    ACCOUNT_TEXT_FIELD = (By.ID, "identifierId")
    ACCOUNT_NEXT_BUTTON = (By.ID, "identifierNext")
    PASSWORD_TEXT_FIELD = (By.NAME, "Passwd")
    PASSWORD_NEXT_BUTTON = (By.ID, "passwordNext")

class GoogleMailLoginPage(BasePage):
    gmail_login_page_locators = GoogleMailLoginPageLocators

    def get_gmail_page(self):
        url = "https://www.gmail.com"
        self.get_page(url)

    def input_user_account(self):
        self.find_element(self.gmail_login_page_locators.ACCOUNT_TEXT_FIELD).send_keys(TestMailAccount.USER_ACCOUNT)
        self.find_element(self.gmail_login_page_locators.ACCOUNT_NEXT_BUTTON).click()

    def input_user_password(self):
        self.find_element(self.gmail_login_page_locators.PASSWORD_TEXT_FIELD).send_keys(TestMailAccount.USER_PASSWORD)
        self.find_element(self.gmail_login_page_locators.PASSWORD_NEXT_BUTTON).click()








