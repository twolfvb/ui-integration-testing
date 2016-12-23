# Test de integración

Los test de integración son aquellas pruebas que se realizan una vez que se hayan aprobado los test unitarios para comprobar que cada componente del software funcionan correctamente como sistema.

En el marco del curso CC6402-1 Taller Avanzado de Desarrollo Ágil y Lean se realizó un proyecto cuyo objetivo principal era introducir a los estudiantes a desarrollar una ToDoList utilizando la metodología Test Driven Development (TDD). Uno de los pasos del TDD era realizar pruebas unitarias a los distintos componentes del sistema, es decir se verificaba su funcionamiento. Si bien se testeaba cada componente, existían problemas a la hora de realizar pruebas en la interfaz, dado que la Suit de Test de Django estaba limitada a solo ver el contenido de la página.

Selenium es una herramienta que permite hacer pruebas en la interfaz web de una aplicación. Por ejemplo puede realizar las siguientes instrucciones:

- Cargar la página
- Completar un formulario
- Enviar el formulario mediante el botón *Enviar*
- Cerrar una ventana de información

La herramienta permite simular el comportamiento del usuario, con ello se pueden realizar test más sofisticados que permiten ver el funcionamiento correcto del sistema.

Se integró Selenium en el proyecto ToDoList y se realizaron una serie de Test de integración.

# Instalación

Descargar [ToDoList](https://github.com/Claudin/todolist) y ejecutar los siguientes comandos.
```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Descargar [ui-integration-testing](https://github.com/twolfvb/ui-integration-testing) y ejecutar los siguientes comandos

Instalar Selenium.
```sh
$ pip install selenium
```
Para ejecutar los scripts debe estar corriendo la aplicación TodoList en *localhost:8000*
```sh
$ python test_nombretest.py
```

Al momento de ejecutar el comando se abrirá el browser y comenzará a ejecutar cada unos de los test listados en el script.


# Trabajo a futuro

El trabajo realizado fue solo para probar la herramienta y el resultado es positivo, pero abre muchas llaves para seguir explorando:

- Empaquetar el funcionamiento por componentes, es decir crear pequeñas librerías que simplifiquen el funcionamiento por componentes.
- ...
