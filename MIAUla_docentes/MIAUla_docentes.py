from MIAUla_docentes_inicio_de_sesion import iniciar_sesion
from MIAUla_docentes_cambiar_contraseña import cambiar_contraseña
from MIAUla_docentes_registro import docente_registro

print("__________________________________________________________________")
print("Bienvenido a MIAUla ¡Tu camino academico!")
print(" ")

def pedir_opcion():
    while True:
        try:
            opcion=int(input("Ingresa la opcion: "))
            print(f"Su opcion es {opcion}")
            return opcion
        except:
            print(" ")
            print("La opcion debe de ser un numero")
            print(" ")

#Evaluamos y mandamos a llamar a la funcion dependiendo de la opcion elegida
while True:
    print(" ")
    print("Elige una opcion, si ya estas registrado puedes iniciar sesion o si eres nuevo puedes registrarte")
    print("__________________________________________________________________")
    print(" ")
    print("__________MENU PRINCIPAL__________")

    print(" ")
    print("1. Iniciar sesion")
    print("2. Cambiar contraseña")
    print("3. Registrarte")
    print("4. Salir")
    print(" ")

    #pedimos la opcion
    opcion=pedir_opcion()
    
    if opcion==1:
        iniciar_sesion()
    if opcion==2:
        cambiar_contraseña()
    if opcion==3:
        docente_registro()
    if opcion==4:
        break
    if opcion not in (1, 2, 3, 4):
        print("Solo existen 4 opciones. Intenta de nuevo")