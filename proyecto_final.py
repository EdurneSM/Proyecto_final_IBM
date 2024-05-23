################################################
########## GESTOR DE TAREAS PENDIENTES #########
########### Creado por: Edurne Sáenz ###########
################################################

################################################
# TAREAS PERMITIDAS AL USUARIO:
# - Agregar nueva tarea
# - Marcar una tarea como completada
# - Mostrar todas las tareas con su estado
# - Eliminar tareas
################################################


# Creo una lista que imita a los elementos de la lista de tareas
#  Contiene POSICIÓN - NOMBRE - ESTADO
""" Tengo:
- Tareas --> con posición, nombre y estado
- Lista --> con las tareas
- Menú --> con las opciones para el usuario"""

###############################################################################################
# Defino la clase tarea, con nombre y estado
class Tarea:
    def __init__(self, nombreTarea, is_completa = False):
        self.nombreTarea = nombreTarea
        self.is_completa = is_completa
        self.posicion = None
    
    def __str__(self):
        estado = "Completada" if self.is_completa else "Pendiente" 
        return f"{self.posicion}. {self.nombreTarea} - {estado}"

###############################################################################################
# Defino la clase lista de tareas, que contendrá las tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregarTarea(self):
        nombreTarea = input("Añade una nueva tarea a tu lista: ").strip()
        nuevaTarea = Tarea(nombreTarea)
        self.tareas.append(nuevaTarea)
        self.actualizarPosicion()
        print(f"La nueva tarea se ha añadido correctamente a tu lista\n")
        print(f"Esta es tu lista de tareas actualizada:")
        self.mostrarTareas()
        # print("Has dejado el nombre de la tarea en blanco. Intenta escribir algo.")        Para la excepción
        
    def actualizarPosicion(self):
        for i, tarea in enumerate(self.tareas, start = 1):
            tarea.posicion = i

    def mostrarTareas(self):
        if not self.tareas:
            print("Todavía no hay ninguna tarea en tu lista")
        else:
            for tarea in self.tareas:
                print(tarea)
    
    def estadoCompletada(self, posicion):
        if 0 < posicion <=len(self.tareas):
            self.tareas[posicion -1].is_completa = True
            print(f"Has marcado la tarea {posicion} como completada\n")
            print(f"Esta es tu lista de tareas actualizada:")
            self.mostrarTareas()
        else:
            print("El número de tarea que has introducido no es válido")
    
    def eliminarTareas(self, posicion):
        if 0 < posicion <=len(self.tareas):
            tareaEliminada = self.tareas.pop(posicion - 1)
            self.actualizarPosicion()
            print(f"Has eliminado la tarea '{tareaEliminada.nombreTarea}'")
            print(f"Esta es tu lista de tareas actualizada:")
            self.mostrarTareas()
        else:
            print("El número que has introducido no es un número de tarea correcto")


######################################################################################################
# Clase con el menú
class Menu:
    def __init__(self):
        self.listaTareas = ListaTareas()
        
    def mostrarMenu (self):
        while True:
            print("\n=======================================================\n"
                "¡¡¡BIENVENIDO A TU LISTA DE TAREAS PERSONALIZABLE!!!\n"
                "\nEstas son todas las opciones que tienes:\n"
                "\n[A] Agregar una tarea nueva\n"
                "[C] Marcar una tarea como completada\n"
                "[E] Eliminar una tarea de la lista\n"
                "[M] Mostrar todas las tareas de la lista\n"
                "[S] Salir del menú\n"
                "=======================================================\n")
            eleccion = input("Por favor, selecciona una opción: ").strip().upper()
            
            if eleccion == "A":
                self.listaTareas.agregarTarea()
            elif eleccion == "C":
                try:
                    pos = int(input("Indica el número de la tarea que quieres marcar como Completada: "))
                    self.listaTareas.estadoCompletada(pos)
                except ValueError:
                    print("No hay ninguna tarea con ese número. Por favor, introduce un número de tarea válido")
            elif eleccion == "E":
                try:
                    pos = int(input("Indica el número de la tarea que quieres eliminar de tu lista: "))
                    self.listaTareas.eliminarTareas(pos)
                except ValueError:
                    print("No hay ninguna tarea con ese número. Por favor, introduce un número de tarea válido")
            elif eleccion =="M":
                self.listaTareas.mostrarTareas()
            elif eleccion == "S":
                print("¡Hasta la próxima!")
                break
            else:
                print("La opción seleccionada no es válida. Por favor, indica qué quieres hacer")

# Para probar las funciones 
menu = Menu()
menu.mostrarMenu()
