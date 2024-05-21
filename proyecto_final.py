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


# Declaración de una clase tarea, que contendrá datos sobre la posición en lista, nombre y estado de cada tarea
class Tarea:
    def __init__(self, posicion, nombreTarea, is_completa = False):
        self.posicion = posicion
        self.nombreTarea = nombreTarea
        self.is_completa = is_completa
    
    def __str__(self):
        estado = "Completada" if self.is_completa else "Pendiente" 
        return f"{self.posicion}. {self.nombreTarea} - {estado}"




############################################################################################################################
# Declaración de la clase "Menú", que contiene todas las opciones que se mostrarán al usuario
class Menu:
    def __init__(self):
        pass
        
    def mostrarMenu (self):
        print("=======================================================\n"
            "¡¡¡BIENVENIDO A TU LISTA DE TAREAS PERSONALIZABLE!!!\n"
              "\nEstas son todas las opciones que tienes:\n"
              "\n[A] Agregar una tarea nueva\n"
              "[C] Marcar una tarea como completada\n"
              "[E] Eliminar una tarea de la lista\n"
              "[M] Mostrar todas las tareas de mi lista\n"
              "[S] Salir del menú\n"
              "=======================================================")
        
    def ejecutarOpcion (self):
        opcionUsuario = input("¿Qué deseas hacer? Selecciona una opción: ")
        if opcionUsuario == "A":
            tarea = input("Escribe tu nueva tarea: ")
        # elif opcionUsuario == "C":
        #     tarea = 
        elif opcionUsuario == "E":
            # poner código de borrar elemento
        elif opcionUsuario == "M":
            print(lista)
        else:
            
# Creado para probar si se imprime el menú - puede que tenga que borrarlo
menu = Menu
menu.mostrarMenu(0)
