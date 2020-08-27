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