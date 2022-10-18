class Version:

    def __init__(self):
        self.version_info()

    def version_info(self):
        self.welcome_message = '''
          -Bienvenido a World Of Warcraft Register-

    Este programa fue creado con el propósito de apoyar a
    farmers del WoW en llevar un registro ordenado y 
    legible de sus ingresos.

    VERSIÓN ACTUAL = 2.0

    Actualizaciones:

1 - Cuando se va a editar un registro, ahora se podrán
   ver los valores actuales en las cajas de texto.

2 - Se prohibió el uso de caracteres (a,b,c...). 
   Adicionalmente, se prohibió ingresar un día mayor
   a 31 y un mes mayor a 12.

3 - Se agregó la opcion de colocar una fecha actual 
   o una fecha personalizada.

4 - Se deshabilitó el campo del total. 
   Adicionalmemte, se sustituyó el valor
   "None" por el valor "0".

5 - Se arreglaron varios bugs de texto y 
   posicionamiento de elementos.

6 - Se añadió un nuevo cálculo a la calculadora.

7 - Nueva funcionalidad añadida: 

   -Filtrar-

   Ahora los usuarios que deseen ingresar una
   gran cantidad de registros podran trabajar de 
   una forma mucho mas específica y cómoda.

   Actualmente, posee la capacidad de filtrar por
   ID, Cantidad de Farmeo y Tiempo.

   En la parte superior de la pestaña "Registros" 
   hay 2 campos, en los que podrás seleccionar
   por cuál columna se va a filtrar e ingresar
   el valor que deseas buscar. 

   Posteriormente, al presionar el botón "Filtrar"
   se abrirá una nueva ventana con la información
   de los registros coincidentes con la búsqueda.

8 - ¡Nuevo ícono!

    ¡Espero les guste!

    - JIZ Dsing 

    Soporte / Contacto: jizdsing@gmail.com
        '''

        return self.welcome_message

    def __str__(self):
        message = self.welcome_message
        return message



