# Curso-de-introduccion-a-Selenium-con-Python
Curso de introduccion a Selenium con Python realizado en Platzi

**Contenido**

[Clase 1 Bienvenida al curso](#Clase-1-Bienvenida-al-curso)

[Clase 2 Historia de Selenium](#Clase-2-Historia-de-Selenium)

[Clase 3 Otras herramientas de testing y automatización](#Clase-3-Otras-herramientas-de-testing-y-automatización)

[Clase 4 Configurar entorno de trabajo](#Clase-4-Configurar-entorno-de-trabajo)

[Clase 5 ¡Hola, Mundo!](#Clase-5-¡Hola-Mundo!)

[Descarga del archivo y el Chrome Driver](#Descarga-del-archivo-y-el-Chrome-Driver)

[Clase 6 Encontrar elementos con find_element](#Clase-6-Encontrar-elementos-con-find_element)

[Clase 7 Preparar assertions y test suites](#Clase-7-Preparar-assertions-y-test-suites)

[Clase 8 Entender las clases WebDriver y WebElement](#Clase-8-Entender-las-clases-WebDriver-y-WebElement)

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

[]()

## Clase 1 Bienvenida al curso

Recomendaciones de cursos antes de iniciar con el de Selenium

- Curso de Introduccion al pensamiento computacional con Python 

- Curso de Programación Orientada a Objetos: POO

- Curso de desarrollo web online

- Curso de fundamentos de pruebas de software

## Clase 2 Historia de Selenium

**¿Qué es selenium?**

Es una "Suite de herramientas para automatizacion de navegadores", tambien es asociado a testing o web scraping

Selenium es compatible con navegadores como Firefox, Internet explorer, Google Chrome, Opera, Safari 

Tambien es compatible con distintos lenguajes de programacion como JAVA, C# Ruby, Python, PHP, JavaScript, PERL y Kotlin

Selenium **No es una herramienta de testing o web scraping**, se puede utilizar para esas tareas pero su desempeño en las mismas puede no ser el optimo

![assets/img1.png](assets/img1.png)

![assets/img2.png](assets/img2.png)

![assets/img3.png](assets/img3.png)

**Origen del nombre**

![assets/img4.png](assets/img4.png)

La compañia de desarrollo que creo Selenium originalmente tenia un competidor llamado Mercurial.
Cuando una persona padece intoxicación por mercurio debe consumir suplementos hechos a base de selenio para poderse curar.

Entonces el equipo de desarrollo considero una buena idea utilizar el nombre de Selenium porque como tal ofrecian una cura para lo que este competidor hacia u ofrecia.

**Caracteristicas, pros y contras de Selenium IDE**

**Pros**

- Excelente para iniciar en testing y pruebas unitarias teniendo en cuenta que funciona a base de clicks en los elementos del sitio web 

- No requiere saber programar lo que lo hace bastante util para novatos

- Exporta Scripts para Selenium RC(remote control) y Selenium WebDriver

- Genera reportes como cuanto duro una prueba, que acciones se tomaron, errores y fallas que hubo durante las pruebas

**Contras**

- Disponible solo para Firefox y Chrome

- No soporta DDT(Data-Driven-Testing), no es posible colocar datos para realizar multiples pruebas

**Caracteristicas, pros y contras de Selenium RC(Remote Control)**

**Pros**

- Soporte para varias plataformas, navegadores y lenguajes de programacion

- Operaciones logicas y condicionales cuando realizamos pruebas

- soporta DDT(Data-Driven-Testing)

- **Posee una API madura** con la que se puede llevar a cabo metodos y funciones que hacen mas agiles las pruebas

**Contras**

- Complejo de instalar (requiere instalar varios archivos)

- Necesita de un servidor corriendo (con el cual se comunica antes de poder enviar las interacciones al navegador)

- Comandos redundantes en su API (Pueden parecer a metodos que hagan lo mismo, pero por debajo funcionan de manera distinta)

- Navegacion no tan realista (Es mas robotica y rigida)

**Caracteristicas, pros y contras de Selenium WebDriver(Herramienta a utilizar en el curso)**

**Pros**

- Soporte para multiples lenguajes

- Facil de instalar

- Comunicación directa con el navegador (No requiere de un servidor intermedio)

- Interacción más realista (Como pensar que hace una persona y trasladarlo a Selenium)

**Contras**

- No soporta nuevos navegadores tan rápido o nuevas actualizaciones

- No genera reportes o resultados de pruebas

- Requiere de saber programar

**Selenium Grid**(Es un complemento)

**Caracteristicas**

- Se utiliza junto a Selenium RC(Remote Control)

- Permite correr pruebas en paralelo

- Conveniente para ahorrar tiempo

## Clase 3 Otras herramientas de testing y automatización

Selium puede no ser la herramienta de testing y automatizacion mas eficiente por lo cual hay que considerar la existencia de otro tipo de herramientas

**Puppeteer**

![assets/img5.png](assets/img5.png)

Tiene una comunidad pequeña por lo cual aun se esta desarrollando 

**Cyperss.io**

![assets/img6.png](assets/img6.png)

Una de sus ventajas mas importantes es que tiene un excelente manejo del asincronimo lo cual hace que las esperas puedan ser dinamicas y se puedan manejar de forma sencilla

**¿Cuál es la mejor opción?**

Se debe tomar en cuenta lo siguiente

- ¿Cuál es lenguaje de programación con el que mas esta familiarizado?

- ¿Qué lenguaje de programación utiliza el equipo de trabajo?

- El proyecto de trabajo requiere grandes llamadas de asincronismo o no

- Si se quiere hacer una automatizacion para hacer una tarea mas sencilla

**Porque usar Selenium durante el curso**

- Facil de utilizar

- Es compatible con muchos navegadores

- Se pueden implementar diversos lenguajes de programación que para el caso sera Python

- Se pueden lograr grandes procesos de automatización y testing

## Clase 4 Configurar entorno de trabajo

![assets/img7.png](assets/img7.png)

Pasos a ejecutar en la terminal estos sirven para entornos en Linux mint, basados en ubuntu o debian.

Tener en cuenta verificar si se pueden seguir los mismos pasos en windows

**paso 1**

python3 --version (se debe tener una version igual o superior a Python 3.6)

**paso 2** 

pip3 install selenium

- en caso de que no este instalado pip

    - sudo apt-get install python3-pip
    - nuevamente ejecutar (pip3 install selenium)

**paso 3**

pip3 install pyunitreport

**pyunitreport es una libreria que sirve para generar reportes en html**

## Clase 5 ¡Hola, Mundo!

Con las herramientas ya instaladas se descarga un archivo adicional que es el driver del navegador para comunicar Selenium con el mismo pero antes hay que revisar conceptos pertenecientes a Unittest que pertenece a una libreria de Python con la cual se realizan pruebas unitarias para obtener la informacion de lo que ocurre con las automatizaciones

![assets/img8.png](assets/img8.png)

- **Test Fixture**

Es todo lo que va a ocurrir antes y despues de una automatización y despues realiza una serie de acciones cuando termine el caso de prueba que se esta realizando

**Test Case** 

Es una unidad de codigo con el cual se indica a selenium que es lo que se requiere hacer o en su defecto alguna funcion que se quiere hacer

**Test Suite**

Es la coleccion de distintas pruebas o automatizaciones en un solo archivo para que se puedan ejecutar todos de forma secuencial

**Test Runner**

Es la parte que se va a encargar de dirigir que se va a ejecutar, en que orden, como y resultados a brindar

**Test Report**

Es la parte que va a mostrar por ejemplo cuantas pruebas corrieron, tiempo de ejecucion, si hubo errores o no

### Descarga del archivo y el Chrome Driver

![assets/img9.png](assets/img9.png)

Descargar la version mas reciente 

![assets/img10.png](assets/img10.png)

Opciones para el sistema operativo

![assets/img11.png](assets/img11.png)

Extraer el archivo preferiblemente en la carpeta en al que se este realizando el curso

Luego abrir el editor de codigo que se tenga y guardar dentro de la carpeta 

un archivo llamado hello_world.py

y a continuacion escribir las siguientes instrucciones:

```
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)

    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
```

import unittest, esta libreria nos sirve para traer todas nuestras pruebas

from pyunitreport import HTMLTestRunner, Nos ayuda a orquestar cada una de las pruebas que estamos ejecutando junto con los reportes

from selenium import webdriver, Desde el modulo de Selenium se importa webdriver para comunicarnos con el navegador

class HelloWorld(unittest.TestCase): Hace referencia a los casos de prueba con unittest.TestCase

Despues vienen los Test Fixture que van a estar definidos como metodos y como lo indica la sintaxis

A continuacion se indica que self.driver es igual a webdriver y el nombre del navegador que en este caso es Chrome y se pasa como parametro la ruta de ejecucion del archivo del driver descargado en la carpeta del curso

luego con la palabra driver se hace igual a self.driver para no estar escribiendo en cada linea self.driver

y luego a traves de driver.implicitly_wait(10) que espere implicitamente 10 segundos antes de realizar la siguiente accion

```
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)
```

El siguiente metodo debe iniciar con la palabra test para que asi la pueda identificar el Test Runner

nuevamente con la palabra driver se hace igual a self.driver para no estar escribiendo en cada linea self.driver

y se le indica a traves de driver.get que traiga la direccion que se quiere analizar

```
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')


```
Este es el otro Test Fixture que va dar la salida a lo que estemos escribiendo

Esto es para cerrar la ventana del navegador para evitar una fuga de recursos o que el navegador pueda ponerse lento

```
    def tearDown(self):
        self.driver.quit()
```

Dentro del metodo main se pasan las banderas verbosity, testRunner para que genere los reportes correspondientes

```
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
```

Asi queda el archivo como tal 

![assets/img12.png](assets/img12.png)

Luego de esto pasar a la terminal y ejecutar el archivo que lo que va a hacer es abrir el navegador Chrome, segundos despues se cierra y aparece el reporte

![assets/img13.png](assets/img13.png)

añadir a este mismo archivo despues del metodo test_hello_world, el metodo

```
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')
```

![assets/img16.png](assets/img16.png)


ejecutar en la terminal y por ultimo dentro de la carpeta del curso se va a generar una carpeta llamada reports que contiene a reportes y esta carpeta tiene un archivo llamada hello-world-report.html.

![assets/img17.png](assets/img17.png)

![assets/img14.png](assets/img14.png)

abrir con Chrome para visualizar el reporte donde aparece la duracion y el estatos si paso o fallo 

![assets/img15.png](assets/img15.png)

para que las ventanas no se ejecuten por aparte se hace un cambio y se implementa el decorador classmethod al inicio y finalizacion del Test Fixture y ademas se cambian todas las palabras self por cls


```
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):


    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')


    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')
    

    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

```

y nuevamente se pasa a ejecutar como en los pasos anteriores

## Clase 6 Encontrar elementos con find_element

el siguiente paso es encontrar e identificar cada uno de los elementos que componen a un sitio web para que podamos interactuar con ellos

![assets/img18.png](assets/img18.png)

los selectores seran los que nos den la oportunidad de llegar a los elementos a traves del codigo y ejecutar las acciones que le indiquemos a Selenium

la forma en la que podemos encontrarlos es a traves de:

![assets/img19.png](assets/img19.png)

pagina a analizar http://demo-store.seleniumacademy.com/

La estructura de codigo basica para hacer automatizaciones es la siguiente

```
import unittest

from selenium import webdriver

class HomePageTest(unittest.TestCase):
    

    def setUp(self):
        pass


    def tearDown(self):
        pass


if __name__ == "__main__":
    pass
```

Se crea el codigo a traves de un archivo llamado searchtests.py a continuacion dejo el codigo de esta clase porque en la siguiente cambia la clase y los metodos

**searchtests.py**

```
import unittest

from selenium import webdriver

class HomePageTest(unittest.TestCase):


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")


    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")


    def test_search_button_ennabled(self): 
        button = self.driver.find_element_by_class_name("button")


    def test_count_of_promo_banner_images(self):#Metodo para contar cuantas imagenes hay de promocion en el banner
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
```


Las siguientes lineas de codigo se relacionan con las busquedas de las imagenes que tambien se encuentran en el archivo

**Busqueda de la barra de busqueda**

![assets/img20.png](assets/img20.png)

**Busqueda por el Id**

```
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

```
**Busqueda por el nombre**

```
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

```

**Busqueda por la clase**

```
   def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

```

**Busqueda para verificar que el boton de la barra de busqueda este disponible**

![assets/img21.png](assets/img21.png)

**Busqueda por la clase**

```
    def test_search_button_ennabled(self): 
        button = self.driver.find_element_by_class_name("button")
```

**Busqueda para listar imagenes de las promos de la pagina**

![assets/img22.png](assets/img22.png)

***por la clase y el selector**

```
    def test_count_of_promo_banner_images(self):#Metodo para contar cuantas imagenes hay de promocion en el banner
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))
```

**Busqueda de la imagen principal del banner**

![assets/img23.png](assets/img23.png)

**Busqueda por el Xpath**

```
def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
```
**Busqueda del carro de compras a traves de css**

![assets/img24.png](assets/img24.png)

```
def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
```

Luego ejecutar el archivo en la terminal para verificar que se realicen los test

![assets/img25.png](assets/img25.png)

Tener en cuenta que el Xpath puede no ser la mejor opcion porque las rutas pueden cambiar

## Clase 7 Preparar assertions y test suites

Assertions son los métodos que permiten validar un valor esperado en la ejecución del test. Si el resultado es verdadero el test continúa, en caso contrario "falla" y termina.

![assets/img26.png](assets/img26.png)

Son una coleccion de pruebas unificadas en un archivo como por ejemplo tener pruebas del login, del home y otras secciones. Pero en lugar de estar corriendo un archivo de forma independiente y esperar que termine, se puede unificar en un test suite el cual al correr las pruebas no se van a ejecutar en paralelo, si no, de forma secuencial

Para esta clase se crean varios archivos que son **assertions.py**, **searchtests.py**(el cual es de la clase anterior pero cambian algunas cosas del codigo) y **smoketests.py**, a continuacion dejo los codigos de cada uno en el orden que fueron mencionados

**assertions.py**

```
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
        
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
          
    def tearDown(self):
        self.driver.quit()
        
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
```

**Para la clase 7 el codigo cambia en los archivos por lo cual los dejare entre comentarios por si hay alguna duda y se pueda ejecutar el codigo**

**searchtests.py**

```
import unittest

from selenium import webdriver

class SearchTests(unittest.TestCase):
    

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()


    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
```


**smoketests.py**


```
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#Construccion de suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

#Respecto a los reportes

kwargs = {
    "output": 'smoke-report'
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
```
Despues de grabar estos archivos se ejecuta el archivo smoketests.py para ver que estan corriendo OK. apoyarse igualmente de los videos de Platzi para comprender mejor el codigo 

## Clase 8 Entender las clases WebDriver y WebElement

Como viste en clases anteriores, un sitio web se construye por código **HTML** en forma de árbol, conteniendo distintos elementos con los que podemos interactuar según estén presentes o no en nuestra interfaz gráfica.

**Selenium WebDriver** nos brinda la posibilidad de poder referirnos a estos elementos y ejecutar métodos específicos para realizar las mismas acciones que un humano haría sobre los mismos, gracias a las clases **WebDriver** y **WebElement**.

**Clase WebDriver**

Cuenta con una serie de propiedades y métodos para interactuar directamente con la ventana del navegador y sus elementos relacionados, como son pop-ups o alerts. Por ahora nos centraremos a las más utilizadas.

**Propiedades de la clase WebDriver**

Estas son las más comunes para acceder al navegador.

![assets/img27.png](assets/img27.png)

**Clase WebElement**

Esta clase nos permite interactuar específicamente con elementos de los sitios web como textbox, text area, button, radio button, checkbox, etc.

**Propiedades más comunes de la clase WebElement**

![assets/img28.png](assets/img28.png)

**Métodos más comunes de la clase WebElement**

![assets/img29.png](assets/img29.png)

![assets/img30.png](assets/img30.png)

## Clase 9 Manejar form, textbox, checkbox y radio button

Para esta clase lo que se va a realizar es validar que tanto los campos como las validaciones de ingresos de formulario para crear una cuenta esten de manera correcta. verificar video y a continuacion el archivo el cual se llama **register_new_usser.py**, posteriormente ejecutarlo en la consola para comprobar que es lo que se esta realizando en cada paso

``
import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)


        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed') 
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')


        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Test')
        last_name.send_keys('Test')
        middle_name.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        news_letter_subscription.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)
``