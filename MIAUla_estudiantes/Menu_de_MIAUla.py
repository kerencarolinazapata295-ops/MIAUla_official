def menu():
    print("1. Iniciar sesion")
    print("2. Cambiar contraseña")
    print("3. Registrarte")
    print("4. Salir")

def menu_de_inicio():
    print(" ")
    print("__________Pagina principal__________")
    print(" ")
    print("1. Entregar tareas")
    print("2. Buscar tarea")
    print("3. Inscribirse a una aula")
    print("4. Mi perfil")
    print("5. Todas las tareas")
    print("6. Cerrar sesion")

def limpiar(x):
    return " ".join ((x).strip().lower().split()).title()

def pedir_opcion():
    while True:
        try:
            opcion=int(input("Ingresa la opcion: "))
            print(f"Su opcion es {opcion}")
            return opcion
        except:
            print("La opcion debe de ser un numero")