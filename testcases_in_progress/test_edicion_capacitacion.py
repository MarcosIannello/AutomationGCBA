# import unittest
# import commons_backoffice
# import commons_web
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By
#
#
# #variables para completar campos
# user_bo = "11111111111"
# password = "Troquel1"
# codigocapacitacion = "2022"
# nombrecapacitacion = "altaCapacitacionAutomatizada"
# detallecapacitacion = "prueba alta automatizada"
# enlacedeimagen = "https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/04/Actualizacion-en-administracion-de-consorcios.jpg"
# contenidoscapacitacion = "aca se visualizaran los contenidos de una capacitacion"
# abc = "abc"
#
#
# #locators
# boton_cursos = "//a[text()= 'Ver todos']"
# filtro_nombre_web = "//input[@id='name-input']"
# boton_buscar_web = "//button[@id='btn-search']"
# filtro_nombre_bo = "//input[@id='SearchCapacitacionType_nombre']"
# capacitaciones = "//a[@id='capacitaciones']"
# boton_crear = "//button[@class='btn btn-primary']"
# cerrar_menu_lateral = "//span[@class='navbar-toggler-icon']"
# campo_programa = "(//div[@class='filter-option-inner-inner'][normalize-space()='Seleccionar...'])[1]"
# opcion_programa = "//span[normalize-space()='Digitalizate']"
# campo_codigo_capacitacion = "//input[@id='CapacitacionType_codigo']"
# campo_nombre_capacitacion = "//input[@id='CapacitacionType_nombre']"
# campo_detalle_capacitacion = "//textarea[@id='CapacitacionType_detalle']"
# seleccion_tipo_imagen = "(//input[@name='tipoImagen'])[2]"
# input_url_imagen= "(//input[@name='tipoImagen'])[2]"
# campo_tipo_formacion =  "//button[@data-id='CapacitacionType_tipoFormacionOrigen']"
# opcion_tipo_formacion = "//span[normalize-space()='Carrera']"
# campo_modalidad = "//button[@data-id='CapacitacionType_modalidad']"
# opcion_modalidad = "//span[normalize-space()='Presencial y Virtual']"
# campo_sector_productivo = "//button[@data-id='CapacitacionType_sectorEstrategico']"
# opcion_sector_productivo = "//span[normalize-space()='ELECTRÓNICA']"
# campo_categoria_web = "//button[@data-id='CapacitacionType_categoriaFront']"
# opcion_categoria_web = "//span[normalize-space()='Electrónica']"
# campo_contenidos = "//div[@id='cke_1_contents']"
# boton_publicar = "//button[normalize-space()='Publicar']"
# boton_buscar_bo = "//button[@class='btn btn-secondary ml-xl-2']"
#
#
# class TestEdicionCapacitacion(commons_backoffice.BaseTest, unittest.TestCase):
#
#     def test_edicion_capacitacion(self):
#
#         self.login_bo(user_bo, password)
#         self.go_to_menus(capacitaciones)
#         self.complete_field(filtro_nombre_bo, nombrecapacitacion)
#         self.click_element(boton_buscar_bo)
#         self.wait_for(5)
#
#

