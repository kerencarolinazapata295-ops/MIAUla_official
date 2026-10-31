import json
import secrets
import string
from pathlib import Path


CARPETA_AULAS = Path(__file__).resolve().parent.parent / "MIAUla_aulas"

CARPETA_AULAS.mkdir(parents=True, exist_ok=True)

#Funciones para crear las aulas

def generar_codigo():
    caracteres = string.ascii_uppercase + string.digits

    while True:
        codigo = "".join(
            secrets.choice(caracteres)
            for _ in range(6)
        )

        archivo = CARPETA_AULAS / f"aula_{codigo}.json"

        if not archivo.exists():
            return codigo

def crear_aula():
    codigo = generar_codigo()

    archivo = CARPETA_AULAS / f"aula_{codigo}.json"

    datos_aula = {
        "codigo_aula": codigo,
        "tareas": [],
        "estudiantes": []
    }

    with open(archivo, "w", encoding="utf-8") as json_file:
        json.dump(
            datos_aula,
            json_file,
            indent=4,
            ensure_ascii=False
        )

    return codigo

def cargar_tareas_aula(codigo_aula):
    archivo = CARPETA_AULAS / f"aula_{codigo_aula}.json"

    if not archivo.exists():
        return None

    with open(archivo, "r", encoding="utf-8") as file:
        return json.load(file)

def guardar_tareas_aula(codigo_aula, tareas):
    archivo = CARPETA_AULAS / f"aula_{codigo_aula}.json"

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(
            tareas,
            file,
            indent=4,
            ensure_ascii=False
        )