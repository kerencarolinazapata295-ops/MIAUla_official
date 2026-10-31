import json
from pathlib import Path
import string
import secrets

CARPETA_AULAS = Path(__file__).resolve().parent.parent / "MIAUla_aulas"

CARPETA_AULAS.mkdir(parents=True, exist_ok=True)


#Funciones principales de MIAUla-Docentes

def obtener_ruta(nombre_archivo): 
    import os
    return os.path.join(os. path.dirname(__file__), nombre_archivo)

def guardar_tareas(codigo_de_aula, datos_aula):
    archivo= CARPETA_AULAS / f"aula_{codigo_de_aula}.json"
    
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos_aula, file, indent=4, ensure_ascii=False)

def generar_codigo(tareas):
    caracteres = string.ascii_uppercase + string.digits

    while True:
        codigo = "".join(
            secrets.choice(caracteres)
            for _ in range(6)
        )

        existe = False

        for tarea in tareas:
            if tarea["id"] == codigo:
                existe = True
                break

        if not existe:
            return codigo

def publicar_tarea(codigo_aula):

    archivo = CARPETA_AULAS / f"aula_{codigo_aula}.json"

    with open(archivo, "r", encoding="utf-8") as file:
        datos_aula = json.load(file)
    print("\n__________ PUBLICAR TAREA __________")

    id_tarea=generar_codigo(datos_aula["tareas"])
    titulo = input("Ingresa el titulo de la tarea: ").strip()
    descripcion = input("Instrucciones: ").strip()
    enlace = input("Enlace de Google Drive: ").strip()

    if not titulo or not enlace:
        print("El título y el enlace son obligatorios.")
        return

    if not enlace.startswith(("https://", "http://")):
        print("El enlace no es válido.")
        return

    tarea = {
        "id": id_tarea,
        "titulo": titulo,
        "descripcion": descripcion,
        "enlace": enlace
    }

    datos_aula["tareas"].append(tarea)
    guardar_tareas(codigo_aula, datos_aula)

    print("Tarea publicada correctamente.")

def todas_las_tareas(codigo_aula):
    archivo = CARPETA_AULAS / f"aula_{codigo_aula}.json"

    with open(archivo, "r", encoding="utf-8") as file:
        datos_aula = json.load(file)

    encontradas = datos_aula["tareas"]

    print("\n__________ TODAS LAS TAREAS __________")

    if not encontradas:
        print("Todavía no has publicado tareas.")
        print(" ")
        return

    for numero, tarea in enumerate(encontradas, start=1):
        print(f"\n{numero}. {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Enlace: {tarea['enlace']}")