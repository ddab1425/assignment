from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from placementsio.base.base_page import BasePage

def replace_param(locator, r, a):
    l1, l2 = locator
    return (l1, l2.replace(r, a))

class GoogleMailInboxPageLocators:
    COMPOSE_BUTTON = (By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div")
    COMPOSE_BOX_RECEIVER_TEXT = (By.XPATH, "//div[@class='aH9']/input")
    COMPOSE_BOX_SUBJECT_TEXT = (By.NAME, "subjectbox")
    COMPOSE_BOX_BODY_TEXT = (By.XPATH, "//table[@id='undefined']/tbody/tr/td[2]/div[2]/div")
    COMPOSE_BOX_MORE_OPTION_BUTTON = (By.XPATH, "//table[@class='IZ']/tbody/tr/td[5]/div[2]")
    COMPOSE_BOX_LABEL = (By.XPATH, "//div[@title='LABEL']")
    COMPOSE_BOX_SEND_BUTTON = (By.XPATH, "//div[@class='dC']/div")
 
    STAR_BUTTON_BY_SUBJECT = (By.XPATH, "//span[@class='bog']/span[text()='SUB']//preceding::td[@class='apU xY']")
    SOCIAL_MAIL_BOX_TAB = (By.XPATH, "//table[@class='aKk']/tbody/tr/td[3]/div")
    SELCT_MAIL_BY_SUBJECT = (By.XPATH, "//span[@class='bog']/span[text()='SUB']")
 
    OPENED_MAIL_SUBEJECT = (By.CLASS_NAME, "hP")
    OPENED_MAIL_BODY = (By.XPATH, "//div[@class='ii gt']/div/div[@dir='ltr']")
    OPENED_MAIL_LABEL_BUTTON = (By.XPATH, "//div[@class='iH bzn']/div/div[4]/div[2]")
    OPENED_MAIL_LABEL_LIST = (By.XPATH, "//div[@class='J-M-Jz aiL']//div[@aria-checked='true']")
    OPENED_MAIL_DELETE_BUTTON = (By.XPATH, "//div[@class='iH bzn']/div/div[2]/div[3]")

class GoogleMailInboxPage(BasePage):
    gmail_inbox_page_locators = GoogleMailInboxPageLocators

    def click_compose_button(self):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BUTTON).click()

    def input_mail_receiver(self, mail_account):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BOX_RECEIVER_TEXT).send_keys(mail_account)

    def input_subject(self, subject):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BOX_SUBJECT_TEXT).send_keys(subject)

    def input_mail_body(self, body):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BOX_BODY_TEXT).send_keys(body)

    def add_mail_label(self, label):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BOX_MORE_OPTION_BUTTON).send_keys(Keys.ENTER + Keys.ARROW_DOWN * 2 + Keys.ENTER)
        locator = replace_param(self.gmail_inbox_page_locators.COMPOSE_BOX_LABEL, "LABEL", label)
        self.find_element(locator).click()

    def click_send_button(self):
        self.find_element(self.gmail_inbox_page_locators.COMPOSE_BOX_SEND_BUTTON).click()

    def star_mail_by_subject(self, subject):
        locator = replace_param(self.gmail_inbox_page_locators.STAR_BUTTON_BY_SUBJECT, "SUB", subject)
        self.find_elements(locator)[-1].click()

    def switch_to_social_mail_box(self):
        self.find_element(self.gmail_inbox_page_locators.SOCIAL_MAIL_BOX_TAB).send_keys(Keys.ENTER)

    def open_mail_by_subject(self, subject):
        locator = replace_param(self.gmail_inbox_page_locators.SELCT_MAIL_BY_SUBJECT, "SUB", subject)
        self.find_element(locator).click()

    def get_opened_mail_subject(self):
        return self.find_element(self.gmail_inbox_page_locators.OPENED_MAIL_SUBEJECT).get_attribute('innerText')

    def get_opened_mail_body(self):
        return self.find_element(self.gmail_inbox_page_locators.OPENED_MAIL_BODY).get_attribute('innerText')

    def get_opened_mail_labels(self):
        self.find_element(self.gmail_inbox_page_locators.OPENED_MAIL_LABEL_BUTTON).send_keys(Keys.ENTER)
        labeled = self.find_elements(self.gmail_inbox_page_locators.OPENED_MAIL_LABEL_LIST)
        return [ele.get_attribute('title') for ele in labeled]

    def delete_opened_mail(self):
        self.find_element(self.gmail_inbox_page_locators.OPENED_MAIL_DELETE_BUTTON).send_keys(Keys.ENTER)











