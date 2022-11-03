import unittest
import commons_backoffice
import commons_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


#variables para completar campos
user_bo = "11111111111"
password = "Troquel1"
codigocapacitacion = "2022"
nombrecapacitacion = "altaCapacitacionAutomatizada"
detallecapacitacion = "prueba alta automatizada"
enlacedeimagen = "https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/04/Actualizacion-en-administracion-de-consorcios.jpg"
contenidoscapacitacion = "aca se visualizaran los contenidos de una capacitacion"
abc = "abc"

#locators
boton_cursos = "//a[text()= 'Ver todos']"
filtro_nombre_web = "//input[@id='name-input']"
boton_buscar_web = "//button[@id='btn-search']"
filtro_nombre_bo = "//input[@id='SearchCapacitacionType_nombre']"
capacitaciones = "//a[@id='capacitaciones']"
boton_crear = "//button[@class='btn btn-primary']"
cerrar_menu_lateral = "//span[@class='navbar-toggler-icon']"
campo_programa = "(//div[@class='filter-option-inner-inner'][normalize-space()='Seleccionar...'])[1]"
opcion_programa = "//span[normalize-space()='Digitalizate']"
campo_codigo_capacitacion = "//input[@id='CapacitacionType_codigo']"
campo_nombre_capacitacion = "//input[@id='CapacitacionType_nombre']"
campo_detalle_capacitacion = "//textarea[@id='CapacitacionType_detalle']"
seleccion_tipo_imagen = "(//input[@name='tipoImagen'])[2]"
input_url_imagen= "(//input[@name='tipoImagen'])[2]"
campo_tipo_formacion =  "//button[@data-id='CapacitacionType_tipoFormacionOrigen']"
opcion_tipo_formacion = "//span[normalize-space()='Carrera']"
campo_modalidad = "//button[@data-id='CapacitacionType_modalidad']"
opcion_modalidad = "//span[normalize-space()='Presencial y Virtual']"
campo_sector_productivo = "//button[@data-id='CapacitacionType_sectorEstrategico']"
opcion_sector_productivo = "//span[normalize-space()='ELECTRÓNICA']"
campo_categoria_web = "//button[@data-id='CapacitacionType_categoriaFront']"
opcion_categoria_web = "//span[normalize-space()='Electrónica']"
campo_contenidos = "//div[@id='cke_1_contents']"
boton_publicar = "//button[normalize-space()='Publicar']"
boton_buscar_bo = "//button[@class='btn btn-secondary ml-xl-2']"


class TestCapacitacion(commons_backoffice.BaseTest, unittest.TestCase):

    def test_alta_capacitacion(self):

        self.login_bo(user_bo, password)
        self.go_to_menus(capacitaciones)

        self.wait_for(5)

        self.click_element(boton_crear)

        self.click_element(cerrar_menu_lateral)

        #seleccion programa
        self.click_element(campo_programa)

        self.click_element(opcion_programa)

        #ingreso codigo capacitacion
        self.complete_field(campo_codigo_capacitacion, codigocapacitacion)

        #ingreso nombre capacitacion
        self.complete_field(campo_nombre_capacitacion, nombrecapacitacion)

        #ingreso_detalle_capacitacion
        self.complete_field(campo_detalle_capacitacion, detallecapacitacion)

        #seleccion enlace imagen
        self.click_element(seleccion_tipo_imagen)
        #ingresar URL imagen
        self.complete_field(input_url_imagen, enlacedeimagen)

        #seleccion tipo_formacion
        self.click_element(campo_tipo_formacion)
        self.click_element(opcion_tipo_formacion)

        #seleccion modalidad
        self.click_element(campo_modalidad)
        self.click_element(opcion_modalidad)

        self.driver.execute_script("window.scrollTo(0, 700)")

        #seleccion sector productivo
        self.click_element(campo_sector_productivo)
        self.click_element(opcion_sector_productivo)

        self.wait_for(3)

        #seleccion categoria web
        self.click_element(campo_categoria_web)
        self.click_element(opcion_categoria_web)

        #ingresar contenidos POR AHORA MANUALMENTE
        self.click_element(campo_contenidos)
        #INTENTAR CORREGIR INGRESO EN CAMPO CONTENIDO
        # WebDriverWait(self.driver, timeout=5).until(
        #     expected_conditions.element_to_be_clickable(
        #         (By.XPATH,
        #          "//iframe[@title='Editor de Texto Enriquecido, CapacitacionType_contenidos']"))
        # ).send_keys(contenidoscapacitacion)

        self.wait_for(2)

        #Redirige final pagina
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #Alta capacitacion
        self.click_element(boton_publicar)

        self.wait_for(5)

        self.complete_field(filtro_nombre_bo, nombrecapacitacion)
        self.click_element(boton_buscar_bo)
        self.clear_field(filtro_nombre_bo)

        self.assertTrue(nombrecapacitacion in self.driver.page_source)


#validacion en web existencia del curso

class TestValidacionWeb(commons_web.BaseTest, unittest.TestCase):

    def test_verificacion_web(self):
        self.wait_for(5)

        self.go_to_cursos(boton_cursos)

        self.wait_for(5)

        self.complete_field(filtro_nombre_web, nombrecapacitacion)

        self.click_search_button(boton_buscar_web)

        self.clear_field(filtro_nombre_web)

        self.wait_for(4)

        self.assertTrue(nombrecapacitacion in self.driver.page_source)



