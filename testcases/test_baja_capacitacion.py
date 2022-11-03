import unittest
import commons_backoffice
import commons_web


#variables
user_bo = "11111111111"
password = "Troquel1"
nombrecapacitacion = 'altaCapacitacionAutomatizada'
filtro_nombre_bo = "//input[@id='SearchCapacitacionType_nombre']"
cartel_eliminacion_exitosa = "Se eliminó capacitacion con éxito"

#locators
capacitaciones = "//a[@id='capacitaciones']"
boton_eliminar = "//button[@data-original-title='Eliminar']"
boton_confirmar_eliminacion = "//button[text()='Eliminar']"
boton_buscar_bo = "//button[@class='btn btn-secondary ml-xl-2']"


class TestBajaCapacitacion(commons_backoffice.BaseTest,unittest.TestCase):

    def test_baja_capacitacion(self):

        self.login_bo(user_bo, password)
        self.go_to_menus(capacitaciones)
        self.wait_for(2)

        self.complete_field(filtro_nombre_bo, nombrecapacitacion)
        self.click_element(boton_buscar_bo)

        self.wait_for(2)

        self.click_element(boton_eliminar)
        self.click_element(boton_confirmar_eliminacion)

        self.wait_for(5)

        self.assertTrue(cartel_eliminacion_exitosa in self.driver.page_source)



