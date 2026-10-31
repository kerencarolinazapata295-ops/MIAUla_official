#Importamos nuestros modulos
from Menu_de_MIAUla import menu,pedir_opcion
from MIAUla_inicio_de_sesion import iniciar_sesion
from MIAUla_cambiar_contraseña import cambiar_contraseña
from MIAUla_registro import registro

print("__________________________________________________________________")
print("Bienvenido a MIAUla ¡Tu camino academico!")


#Evaluamos y mandamos a llamar a la funcion dependiendo de la opcion elegida
while True:
    print(" ")
    print("Elige una opcion, si ya estas registrado puedes iniciar sesion o si eres nuevo puedes registrarte")
    print("__________________________________________________________________")
    print(" ")
    print("__________MENU PRINCIPAL__________")
    print(" ")
    menu()
    print(" ")

    opcion=pedir_opcion()

    if opcion==1:
        iniciar_sesion()
    if opcion==2:
        cambiar_contraseña()
    if opcion==3:
        registro()
    if opcion==4:
        break
    if opcion not in (1,2,3,4):
        print("Solo existen 4 opciones. Intenta de nuevo")