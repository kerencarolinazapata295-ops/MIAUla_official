#Programa apara aceptar a los docentes registrados oficialmente en el programa de MIAUla-Docentes
import json,random,string
from MIAUla_aulas import crear_aula
from MIAUla_docente_funciones_principales import obtener_ruta

ruta_json_pendientes=obtener_ruta("MIAUla_docentes_pendientes.json")
ruta_json_docentes=obtener_ruta("MIAUla_docentes.json")

with open (ruta_json_docentes, "r") as file:
    datos=json.load(file)

with open (ruta_json_pendientes, "r") as archivo:
    base=json.load(archivo)

def guardar():
    with open(ruta_json_docentes, "w") as file:
        json.dump(datos,file, indent=8, ensure_ascii=False)

def guardar_docentes_pendientes():
    with open(ruta_json_pendientes, "w") as archivo:
        json.dump(base,archivo, indent=8, ensure_ascii=False)

def generar_codigo():
    caracteres=string.ascii_uppercase+ string.digits

    while True:
        codigo_generado=''.join(random.choices(caracteres, k=6))
        if codigo_generado not in datos:
            return codigo_generado

print(" ")
print("Confirmacion de docentes de MIAUla 🤝")

while True:
    print(" ")
    print("__________MENU PRINCIPAL__________")
    print("_"*30)
    print(" ")
    print("Elige tu opcion")
    print("1. Aceptar o rechazar usuario")
    print("2. Ver todas las solicitudes")
    print("3. Salir")

    while True:
        try:
            opcion=int(input("Ingresa la opcion: "))
            print(f"Su opcion es {opcion}")
            print("_"*30)
            break
        except:
            print("La opcion debe de ser un numero, intenta de nuevo")
            print("-"*30)
    if opcion==1:

        codigo_temporal=input("Ingresa codigo temporal: ").upper()
        if codigo_temporal in base:
            print("Usuario encontrado con exito ✅")
            print("_"*30)
            
            print("Quieres aceptar o rechazar a este usuario")
            print(" ")
            while True:
                print(" ")
                desicion=input("Elige una opcion, ACEPTAR ||O|| RECHAZAR: ").upper()
                print("_"*30)
                print(" ")
                print(f"Tu opcion elegida fue: {desicion}")
                print(" ")
                if desicion in ("ACEPTAR", "RECHAZAR"):
                    break
                else:
                    print("Error, escribe aceptar o rechazar. Intentalo de nuevo ⚠️")

            if desicion=="ACEPTAR":

                nuevo_codigo_de_docente=generar_codigo()
                codigo_de_aula=crear_aula()
                ficha_docente=base[codigo_temporal].copy()
                ficha_docente.append(codigo_de_aula)
                print(f"{base[codigo_temporal][0]} se le ha sido otorgado el codigo:")
                print("_"*30)
                print(f"Codigo de docente:{nuevo_codigo_de_docente}")
                print("_"*30)
                print(f"Codigo de aula: {codigo_de_aula}")
                print(" ")
                datos[nuevo_codigo_de_docente]=ficha_docente
                del base[codigo_temporal]

                guardar()
                guardar_docentes_pendientes()

            if desicion=="RECHAZAR":
                valor=base.get(codigo_temporal)
                print("-"*100)
                print("_"*20)
                print(f"\nCodigo temporal de docente: {codigo_temporal}")
                print("_"*20)
                print(f"\n Nombre: {valor[0]}")
                print(f"\n Universidad: {valor[1]}")
                print(f"\n Correo electronico: {valor[2]}")
                print(" ") 
                while True:
                    pregunta=input("\nDeseas rechazar a este usuario?\n\nResponde si o no:  ").lower()
                    if pregunta=="si":
                        del base[codigo_temporal]
                        guardar()
                        print("Usuario eliminado con exito ✅")
                        break
                    elif pregunta=="no":
                        print(" ")
                        print("Tu respuesta fue no \n")
                        break
                    else:
                        print("\nSolo existen 2 opciones (si o no). Intenta de nuevo")
        else:
            print("Este codigo no existe")

    elif opcion==2:
        for codigo_de_docente, ficha in base.items():
            print("-"*100)
            print("_"*20)
            print(f"\nCodigo temporal de docente: {codigo_de_docente}")
            print("_"*20)
            print(f"\n Nombre: {ficha[0]}")
            print(f"\n Universidad: {ficha[1]}")
            print(f"\n Correo electronico: {ficha[2]}")
    elif opcion==3:
        break

    else:
        print("Solo existen 2 opciones")
