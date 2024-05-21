# Creo una lista que imita a los elementos de la lista de tareas
#  Contiene POSICIÓN - NOMBRE - ESTADO
""" Tengo:
- Tareas --> con posición, nombre y estado
- Lista --> con las tareas
- Menú --> con las opciones para el usuario"""

###############################################################################################
# Defino la clase tarea, con nombre y estado
class Tarea:
    def __init__(self, posicion, nombreTarea, is_completa = False):
        self.posicion = posicion
        self.nombreTarea = nombreTarea
        self.is_completa = is_completa
    
    def __str__(self):
        estado = "Completada" if self.is_completa else "Pendiente" 
        return f"{self.posicion}. {self.nombreTarea} - {estado}"

###############################################################################################
# Defino la clase lista de tareas, que contendrá las tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    
    def agregarTarea(self):
        while True:
            nombreTarea = input("Añade una nueva tarea a tu lista: ").strip()
            if nombreTarea:
                nuevaPosicion = len(self.tareas) + 1
                nuevaTarea = Tarea(nuevaPosicion, nombreTarea)
                self.tareas.append(nuevaTarea)
                print(f"La nueva tarea se ha añadido correctamente a la lista")
                break
            else:
                print("Has dejado el nombre de la tarea en blanco. Intenta escribir algo.")

    def mostrarTareas(self):
        if not self.tareas:
            print("No hay tareas en tu lista")
        else:
            for tarea in self.tareas:
                print(tarea)
    
    def cambiarEstado(self, posicion):
        if 0 < posicion <=len(self.tareas):
            self.tareas[posicion -1].is_completa = True
            print(f"Has marcado la tarea {posicion} como completada")
        else:
            print("El número de tarea que has introducido no es válido")
    
    def eliminarTareas(self, posicion):
        if 0 < posicion <=len(self.tareas):
            tareaEliminada = self.tareas.pop(posicion - 1)
            print(f"Has eliminado la tarea '{tareaEliminada.nombreTarea}'")
        else:
            print("El número que has introducido no es un número de tarea correcto")


######################################################################################################
# Clase con el menú
class Menu:
    def __init__(self):
        self.lista_tareas = ListaTareas()
        
    def mostrarMenu (self):
        while True:
            print("=======================================================\n"
                "¡¡¡BIENVENIDO A TU LISTA DE TAREAS PERSONALIZABLE!!!\n"
                "\nEstas son todas las opciones que tienes:\n"
                "\n[A] Agregar una tarea nueva\n"
                "[C] Marcar una tarea como completada\n"
                "[E] Eliminar una tarea de la lista\n"
                "[M] Mostrar todas las tareas de mi lista\n"
                "[S] Salir del menú\n"
                "=======================================================")
            eleccion = input("Por favor, selecciona una opción: ").strip().upper()
            
            if eleccion == "A":
                self.lista_tareas.agregarTarea()
            elif eleccion == "C":
                pos = int(input("Indica el número de la tarea que quieres marcar como Completada: "))
                self.lista_tareas.cambiarEstado()
            elif eleccion == "E":
                pos = int(input("Indica el número de la tarea que quieres eliminar de tu lista: "))
                self.lista_tareas.eliminarTareas(pos)
            elif eleccion =="M":
                self.lista_tareas.mostrarTareas()
            elif eleccion == "S":
                print("¡Hasta la próxima!")
                break
            else:
                print("La opción seleccionada no es válida. Por favor, indica qué quieres hacer")

# Para probar las funciones 
menu = Menu()
menu.mostrarMenu()
