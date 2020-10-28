from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BlacklistSearchBase:
    def __init__(self, adres):
        self.adres = adres


class MxToolbox(BlacklistSearchBase):
    def __init__(self, adres):
        super().__init__(adres)

    def searchForBlacklist(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(options=options)

        driver.get('https://mxtoolbox.com/blacklists.aspx')

        search = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput')
        search.clear()
        search.send_keys(self.adres)
        search.send_keys(Keys.RETURN)

        try:
            span = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "tool-result-body"))
            )
            headers = span.find_elements_by_class_name("table-column-Status")
            headers_services = span.find_elements_by_class_name("table-column-Name")
            i = 0
            is_in_list = False

            for head in headers:
                if head.text == " LISTED":
                    print("Girdiginiz adres -", self.adres, "- ", headers_services[i].text, " servisinde kayitlidir.")
                    is_in_list = True
                i += 1
            if not is_in_list:
                print("Girdiginiz adres -", self.adres, "- ", "listede kayitli degil.")
        finally:
            driver.quit()


class UltraTools(BlacklistSearchBase):
    def __init__(self, adres):
        super().__init__(adres)

    def searchForBlacklist(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(options=options)

        driver.get('https://www.ultratools.com/tools/spamDBLookup')

        search = driver.find_element_by_id('domainName')
        search.clear()
        search.send_keys(self.adres)
        search.send_keys(Keys.RETURN)

        try:
            span = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "tool-results-container"))
            )
            headers = span.find_elements_by_tag_name("td")

            i = 0
            is_in_list = False

            while i < len(headers):
                if headers[i].text == "Listed":
                    print("Girdiginiz adres -", self.adres, "- ", headers[i-1].text, " servisinde kayitli olarak bulunmustur.")
                    is_in_list = True
                i += 1

            if not is_in_list:
                print("Girdiginiz adres -", self.adres, "- ", "listede kayitli degil.")
        finally:
            driver.quit()


class WhatIsMyIp(BlacklistSearchBase):
    def __init__(self, adres):
        super().__init__(adres)

    def searchForBlacklist(self):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(options=options)

        driver.get("https://www.whatismyip.com/blacklist-check/")

        try:
            button1 = driver.find_element_by_class_name('navbar-toggler')
            button1.click()

            button2 = driver.find_element_by_css_selector("button[class='btn btn-link pl-0 mr-1 mb-1']")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(button2).click(button2).perform()

            user_input = driver.find_element_by_id("ws-plugin--s2member-pro-login-widget-username")
            user_input.send_keys("izinlihayat@gmail.com")

            psw_input = driver.find_element_by_id("ws-plugin--s2member-pro-login-widget-password")
            psw_input.send_keys("password.dummy12")

            login_btn = driver.find_element_by_css_selector("input[type='submit']")
            login_btn.click()

        except:
            driver.quit()

        driver.get('https://www.whatismyip.com/blacklist-check/')

        search = driver.find_element_by_name('host')
        search.clear()
        search.send_keys(self.adres)
        search.send_keys(Keys.ENTER)

        try:
            span = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
            )
            headers = span.find_elements_by_tag_name("tr")

            for head in headers:
                words = head.text.split()

                if words[0] == "Yes":
                    print("Girdiginiz ", self.adres, " adresi ", words[2], " ", words[3], " servisinde kayitlidir.")

        finally:
            sleep(5)
            driver.quit()
