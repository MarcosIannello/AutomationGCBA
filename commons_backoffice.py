import os
import time
import unittest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

user_bo = "11111111111"
password = "Troquel1"
desplegar_menu_lateral = "//div[@data-target='#educacionCollapse']"
cerrar_menu_lateral = "//span[@class='navbar-toggler-icon']"


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(os.environ.get('APP_URL'))

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def wait_for(seconds):
        time.sleep(seconds)

    def login_bo(self, user, password):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'input#username'))
        ).send_keys(user)

        WebDriverWait(self.driver,timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'input#password'))
        ).send_keys(password)

        self.wait_for(7)

        WebDriverWait(self.driver,timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'button.btn btn-primary'.replace(" ", ".")))
        ).click()

    def go_to_menus(self, menu):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 desplegar_menu_lateral))
        ).click()

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 menu))
        ).click()

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 cerrar_menu_lateral))
        ).click()

        self.wait_for(2)

    def click_element(self, button_selector):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 button_selector))
        ).click()

    def complete_field(self, field_locator, str_value):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 field_locator))
        ).send_keys(str_value)

    def clear_field(self, filter_locator):
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 filter_locator))
        ).clear()




