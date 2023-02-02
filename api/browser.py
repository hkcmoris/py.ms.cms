import json
import os
import mechanicalsoup


class apiBrowser():
    browser = None
    config = []

    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()

    def load(self):
        with open(os.path.join("api", "config.json"), "r") as f:
            self.config = json.load(f)  # load config

    def login(self, username, password):
        page_login = self.browser.open(
            self.config["baseurl"] + self.config["login"])
        if (page_login.status_code != 200):
            print(
                f"{page_login.status_code}\t: {self.config['baseurl']}{self.config['login']}")
            return None

        self.browser.select_form("form")
        self.browser["username"] = username  # admin["user"]
        self.browser["password"] = password  # admin["password"]

        login_response = self.browser.submit_selected()
        if (login_response.status_code != 200 or self.browser.get_url() != "http://www.skolka-riegrova.cz/"):
            print(
                f"{page_login.status_code}\t: {self.config['baseurl']}{self.config['login']}")
            return None

        print(f"Logged in as {username}")
        return True

    def request(self, request):
        if self.browser == None:
            return None

        return request

    def welcomePage(self):
        page = self.browser.open(
            f"{self.config['baseurl']}{self.config['welcome_page']}")
        if (page.status_code != 200):
            print(
                f"{page.status_code}\t: {self.config['baseurl']}{self.config['welcome_page']}")
            return "welcome_page = None"

        return page.soup.find_all('textarea', id='frmarticleEditForm-uvod')[0].text + '\n<hr />\n' + page.soup.find_all('textarea', id='frmarticleEditForm-text')[0].text
