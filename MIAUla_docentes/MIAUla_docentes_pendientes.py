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

        codigo_temporal=input("Ingresa codigo temporal: ")
        if codigo_temporal in base:
            print("Usuario encontrado con exito ✅")
            print("_"*30)
            
            print("Quieres aceptar o rechazar a este usuario")
            while True:
                desicion=input("Elige una opcion, ACEPTAR ||O|| RECHAZAR: ").upper()
                print("_"*30)
                print(f"Tu opcion elegida fue: {desicion}")
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
                del base[codigo_temporal]
                guardar()
                print("Usuario eliminado con exito ✅")
        else:
            print("Este codigo no existe")

    elif opcion==2:
        for codigo_de_docente, ficha in base.items():
            print("-"*100)
            print("_"*20)
            print(f"\nCodigo temporal de docente: {codigo_de_docente}")
            print("_"*20)
            for valor in ficha:
                print(f"\n {valor}")
    elif opcion==3:
        break

    else:
        print("Solo existen 2 opciones")
