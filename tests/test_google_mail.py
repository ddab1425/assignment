from placementsio.pages.google_mail_login import GoogleMailLoginPage
from placementsio.pages.google_mail_inbox import GoogleMailInboxPage
from placementsio.data.google_mail_inbox_data import TestMailData, TestMailAccount
import pytest

@pytest.fixture(scope="module")
def gmail_driver(launch_chrome_driver):
    gmailpage = GoogleMailLoginPage(launch_chrome_driver)
    gmailpage.get_gmail_page()
    gmailpage.input_user_account()
    gmailpage.input_user_password()
    gmailpage = GoogleMailInboxPage(launch_chrome_driver) 

    yield gmailpage

    gmailpage.quit_driver()

class TestGoogleMail:
    def test_send_email(self, gmail_driver):
    	# Send a mail
        gmail_driver.click_compose_button()
        gmail_driver.input_mail_receiver(TestMailAccount.USER_ACCOUNT)
        gmail_driver.input_subject(TestMailData.MAIL_SUBJECT)
        gmail_driver.input_mail_body(TestMailData.MAIL_BODY)
        gmail_driver.add_mail_label(TestMailData.MAIL_LABEL)
        gmail_driver.click_send_button()

        # Verify the received mail
        gmail_driver.switch_to_social_mail_box()
        gmail_driver.star_mail_by_subject(TestMailData.MAIL_SUBJECT)
        gmail_driver.open_mail_by_subject(TestMailData.MAIL_SUBJECT)
        assert gmail_driver.get_opened_mail_subject() == TestMailData.MAIL_SUBJECT
        assert gmail_driver.get_opened_mail_body() == TestMailData.MAIL_BODY
        assert TestMailData.MAIL_LABEL in gmail_driver.get_opened_mail_labels()
        gmail_driver.save_screenshot("verified_received_mail.png")

        # Delete the mail
        gmail_driver.delete_opened_mail()

