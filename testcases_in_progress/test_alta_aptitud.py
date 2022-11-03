import unittest
import commons_backoffice
import commons_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#variables_entorno
user_bo = "11111111111"
password = "Troquel1"
aptitudes = "//a[@id='aptitudes']"
nombre_aptitud = "AltaAutomatizadaAptitud"

#identificadores
campo_nombre_aptitud = "//input[@id='AptitudType_nombre']"
filtro_nombre = "//input[@id='SearchAptitudType_nombre']"
boton_buscar = "//button[@class='btn btn-secondary ml-2']"
boton_crear = "//button[@class='btn btn-primary']"


class TestAltaAptitud(commons_backoffice.BaseTest, unittest.TestCase):

    def test_alta_aptitud(self):

        self.login_bo(user_bo, password)
        self.go_to_menus(aptitudes)
        self.wait_for(2)
        self.click_element(boton_crear)
        self.wait_for(2)
        self.complete_field(campo_nombre_aptitud, nombre_aptitud)
        self.wait_for(2)
        self.click_element(boton_crear)
        self.wait_for(4)
        self.complete_field(filtro_nombre, nombre_aptitud)
        self.click_element(boton_buscar)
        self.wait_for(3)
        self.clear_field(filtro_nombre)

        self.assertTrue(nombre_aptitud in self.driver.page_source)

