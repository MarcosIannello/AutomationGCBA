import os
import time
import unittest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(os.environ.get('APP_URL2'))

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def wait_for(seconds):
        time.sleep(seconds)

    def go_to_cursos(self, cursos_button_locator):
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 cursos_button_locator))
        ).click()

    def complete_field(self, filter_locator, str_variable):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 filter_locator))
        ).send_keys(str_variable)

    def clear_field(self, filter_locator):

        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 filter_locator))
        ).clear()

    def click_search_button(self, button_locator):

        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 button_locator))
        ).click()


