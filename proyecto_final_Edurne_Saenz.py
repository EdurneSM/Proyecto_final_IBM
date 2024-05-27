################################################################
################## GESTOR DE TAREAS PENDIENTES #################
################### Creado por: Edurne Sáenz ###################
################################################################

################################################################
# TAREAS PERMITIDAS AL USUARIO:
# - Agregar nueva tarea
# - Marcar una tarea como completada
# - Mostrar todas las tareas con su estado
# - Eliminar tareas
#################################################################


# Importar Colorama para dar estilo al programa
from colorama import init, Fore, Style
init(autoreset=True)
""" Código de colores a utilizar:
- Azul: menú de opciones
- Verde: mensaje de acción completada con éxito
- Rojo: mensaje de error o excepción"""


# Declaración de la clase Tarea, que incluye el nombre y estado de la tarea, y su posición en una lista de tareas
class Tarea:
    def __init__(self, nombreTarea, is_completa = False):
        self.nombreTarea = nombreTarea
        self.is_completa = is_completa
        self.posicion = None
    
    def __str__(self):
        estado = "Completada" if self.is_completa else "Pendiente" 
        return f"{self.posicion}. {self.nombreTarea} - {estado}"


# Declaración de la clase ListaTareas, que contendrá todas las tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    # Declaración del método para añadir tareas nuevas a la lista
    def agregarTarea(self): # No se incluye nombreTarea como atributo para obligar a que se introduzca con un input
        while True: # Hacemos que el código se ejecute en bucle si el usuario introduce algo en blanco
            nombreTarea = input("Añade una nueva tarea a tu lista: ").strip()
            if nombreTarea: 
                try:
                    nuevaTarea = Tarea(nombreTarea)
                    self.tareas.append(nuevaTarea)
                    self.actualizarPosicion() # Actualizamos la posición de las tareas de la lista
                    print(Fore.GREEN + "✓ La nueva tarea se ha añadido correctamente a tu lista.\n")
                    self.mostrarTareas() # Mostrar cómo queda la lista completa tras la tarea añadida
                    break
                except ValueError:
                    print(Fore.RED + "⚠ Has dejado el nombre de la tarea en blanco. Intenta escribir algo.")
            else:
                print(Fore.RED + "⚠ Has dejado el nombre de la tarea en blanco. Intenta escribir algo.")

    # Declaración del método para actualizar la posición de las tareas en la lista  
    def actualizarPosicion(self):
        for i, tarea in enumerate(self.tareas, start = 1): # Hacemos que la lista empiece en 1 y no en 0
            tarea.posicion = i

    # Declaración del método para mostrar las tareas de la lista (se verá: posición, nombre de la tarea y estado)
    def mostrarTareas(self):
        if not self.tareas:
            print("No hay ninguna tarea en tu lista.")
        else:
            print("Esta es tu lista de tareas actualizada:")
            for tarea in self.tareas:
                print(tarea)

    # Declaración del método para marcar una tarea como completada (el estado inicial es "pendiente")  
    def estadoCompletada(self):
        while True:
            try:
                posicion = int(input("Indica el número de la tarea que quieres marcar como Completada: "))
                if 0 < posicion <=len(self.tareas):
                    self.tareas[posicion -1].is_completa = True
                    print(Fore.GREEN + f"✓ Has marcado la tarea {posicion} como completada.\n")
                    self.mostrarTareas()
                    break
                else:
                    print(Fore.RED + "⚠ El número de tarea que has introducido no es válido.")
            except ValueError:
                print(Fore.RED + "⚠ El número de tarea que has introducido no es válido.")
    
    # Declaración del método para eliminar tareas en la lista  
    def eliminarTareas(self):
        while True:
            try:
                posicion = int(input("Indica el número de la tarea que quieres eliminar de tu lista: ").strip())
                if 0 < posicion <=len(self.tareas):
                    tareaEliminada = self.tareas.pop(posicion - 1)
                    self.actualizarPosicion() # Reordena la numeración de la posición de las tareas en la lista
                    print(Fore.GREEN + f"✓ Has eliminado la tarea '{tareaEliminada.nombreTarea}'.")
                    self.mostrarTareas()
                    break
                else:
                    print(Fore.RED + "⚠ El número que has introducido no es un número de tarea correcto.")
            except ValueError:
                print(Fore.RED + "⚠ El número que has introducido no es un número de tarea correcto.")


# Declaración de la clase Menú, que permite al usuario interactuar con el programa
class Menu:
    # Declaración de una constante con el menú de opciones de usuario
    OPCIONES = """
=======================================================
¡¡¡BIENVENIDO A TU LISTA DE TAREAS PERSONALIZABLE!!!

Estas son todas las opciones que tienes:

[A] Agregar una tarea nueva
[C] Marcar una tarea como completada
[E] Eliminar una tarea de la lista
[M] Mostrar todas las tareas de la lista
[S] Salir del menú
=======================================================
"""
 
    def __init__(self):
        self.listaTareas = ListaTareas()

    # Declaración del método que muestra las diferentes opciones de interacción con el menú  
    def mostrarMenu (self):
        while True: # Con este bucle el menú se ejecutará mientras el usuario introduzca una de las opciones aceptadas en el menú
            print(Fore.BLUE + self.OPCIONES)
            # Obtener la elección del usuario. Incluye upper() para evitar error si el usuario escribe en minúsculas
            eleccion = input("Por favor, selecciona una opción: ").strip().upper()
            
            # Ejecución del condicional IF para movernos por las opciones del menú
            if eleccion == "A":
                self.listaTareas.agregarTarea()
            elif eleccion == "C":
                self.listaTareas.estadoCompletada()
            elif eleccion == "E":
                self.listaTareas.eliminarTareas()
            elif eleccion =="M":
                self.listaTareas.mostrarTareas()
            elif eleccion == "S": 
                print("¡Hasta la próxima! 😃")
                break
            else:
                print(Fore.RED + "⚠ La opción seleccionada no es válida. Por favor, indica qué quieres hacer.")
                # No se incluye la opción "Salir del menú" con los métodos de ListaTareas por ser 
                # una función propia del menú y no implicar cambios en las tareas en sí mismas

    def ejecutarMenu(self):
        while True:
            self.mostrarMenu()
            reiniciar = input("¿Quieres volver a iniciar el programa? (s/n): ").strip().lower()
            if reiniciar != 's':
                print("¡Nos vemos en otra ocasión! 😃")
                break

# Declaración de una instancia de la clase Menú
if __name__ == "__main__": # Incluido para permitir que el código se ejecute si se importa en otro script
    menu = Menu()
    menu.ejecutarMenu()
