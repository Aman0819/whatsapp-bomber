from time import sleep
from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Whatsapp():
    def __init__(self, contact, message=None, times=None):
        self.contact = contact
        self.message = message
        self.times = times

    def login(self):
        self.driver = webdriver.Chrome(
            r"chromedriver.exe")
        self.driver.get("https://web.whatsapp.com")
        self.driver.execute_script('window.alert(arguments[0])', "Scan QR code to continue!")

        try:
            alert = self.driver.switch_to.alert
            sleep(5)
            alert.accept()
        except:
            pass

        print("Logged In")

    def search_for_contact(self):
        self.wait = WebDriverWait(self.driver, 300)
        search_box = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, search_box))).send_keys(self.contact + Keys.ENTER)
        print("Contact Found")

    def send_message(self, message):
        text_box = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        self.driver.find_element_by_xpath(
            text_box).send_keys(message + Keys.ENTER)
        sleep(0.01)

    def single_spam(self):
        self.login()
        self.search_for_contact()
        print("Spamming")

        for _ in range(self.times):
            self.send_message(self.message)


if __name__ == '__main__':

    parser = ArgumentParser(description="Whatsapp Spammer")
    parser.add_argument("-c", required=True,
                        help="Enter the Contact name to be spammed")
    parser.add_argument("-m", required=True,
                        help="Message to spam")
    parser.add_argument("-t", type=int, required=True,
                        help="Number of times to spam")
    args = parser.parse_args()

    Whatsapp(contact=args.c, message=args.m,
             times=args.t).single_spam()
