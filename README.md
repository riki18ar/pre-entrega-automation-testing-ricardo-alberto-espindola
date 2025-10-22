Propósito del proyecto

Automatizar flujos básicos de navegación web utilizando Selenium WebDriver y python en sitio web https://www.saucedemo.com/ .
Las consignas de los casos de pruebas son:
1. Automatización de Login exitoso con credenciales válidas, verificando que se haya redirigido a la página de inventario.
2. Navegación y verificación del catálogo en donde se verifica y valida el título y la presencia de productos.
3. Interacción con productos, añadiendo productos al carrito , verificando y comprobando que el producto se agregue al carrito. 

Tecnologías utilizadas: 
1. Python como lenguaje de programación principal.
2. Pytest como framework de pruebas unitarias sencillas así como también para pruebas funcionales más complejas para la ejecución y generación de informes de casos de prueba.
3. Selenium WebDriver para automatización de la interacción del browser.
4. webdriver-manager que gestiona automáticamente la descarga y uso del chromedriver compatible. 
5. Git y GitHub para control de versiones

Instrucciones de instalación de dependencias
1.  Como prerrequisito tener instalado python3 en tu sistema operativo y navegador Google Chrome.
2.  Clonar el repositorio con el siguiente comando : git clone https://github.com/riki18ar/pre-entrega-automation-testing-ricardo-alberto-espindola.git 
3.  Instalar las dependencias con las librerías necesarias (Selenium, Pytest, webdriver-manager) con el siguiente comando : pip install selenium pytest webdriver-manager

Comando para ejecutar las pruebas 
Una vez instaladas las dependencias, de las pruebas podrán ejecutarse con el siguiente comando : python3 -m pytest -v --html=reports/reporte.html 
Los resultados y evidencia por cada prueba que pase, genera una captura de pantalla y un reporte html.
