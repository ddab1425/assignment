# Assignment 1 
GUI automation for sending and verifying the mail on Gmail page. Implemented with testing framworks `Pytest`, `Selenium` and design pattern `Page Object Model`.
* `Pytest` is used to manage and execute the test cases.
* `Selenium` is used to interact with browser to perform the GUI testing.
* `Page Object Model` is used to design and structure the test scripts. Main concept is to seperate test case and web elements which helps to reduce code duplication and improves test case maintenance.


## Setup
1. cd to the project
2. Run the following command to install requirements.
```bash
pip install -r requirements.txt
```
3. Download the Chrome driver (`chromedriver`) and put it on system path.
4. Prepare a google account and modify the account info at `data/google_mail_inbox_data`.
- Note1: Google account for automation should disable the two step verification
- Note2: Google account's preferred language should be set to English


## Run test
```bash
cd placementsio
pytest tests/test_google_mail.py
or
python -m pytest
```

- This test will verify following:
```
1. Verify the subject and body of the received email
2. Verify the mail having specific label
```

- A screenshot will be generated after execution.
![image](https://github.com/ddab1425/assignment/assets/6958775/4b51128c-93af-416c-aa17-ac62dfafd11a)

## Demo
https://github.com/ddab1425/assignment/assets/6958775/72b5fcf5-962a-4f1d-a4ee-87545740fc25

## My testing environment
```JSON
{
    "Python": "3.11.5", 
    "Platform": "darwin",
    "Packages": 
        {
            "selenium": "4.14.0",
            "pytest": "7.4.3",
            "pluggy": "1.3.0",
            "undetected-chromedriver": "3.5.3"
        }
}
```