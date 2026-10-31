import json
from pathlib import Path

CARPETAS_AULAS=Path(__file__).resolve().parent.parent /"MIAUla_aulas"


#Funciones principales de MIAUla

def obtener_ruta(nombre_archivo): 
    import os
    return os.path.join(os. path.dirname(__file__), nombre_archivo)

def validar_aula(codigo_aula):
    codigo_aula = codigo_aula.strip().upper()

    archivo = CARPETAS_AULAS / f"aula_{codigo_aula}.json"
    print("Carpeta que está buscando:", CARPETAS_AULAS)
    print("Archivo que está buscando:", archivo)

    if not archivo.is_file():
        print("___________________")
        print("Esta aula no existe")
        print(" ")
        return False, "_"

    return True, archivo

def inscribir_estudiante(nombre_de_usuario):
    print("____INSCRIPCION DE ALUMNOS A UNA AULA____")
    print(" ")
    codigo_aula=input("Ingresa codigo de la aula a la que deseas inscribirte: ") 
    print(" ")
    print("_________________________________________")
    valido, resultado = validar_aula(codigo_aula)

    if not valido:
        print(" ")
        print("Esta aula no existe")
        return False, resultado

    archivo = resultado

    with open(archivo, "r", encoding="utf-8") as json_file:
        datos_aula = json.load(json_file)

    for estudiante in datos_aula["estudiantes"]:
        if estudiante["Usuario"] == nombre_de_usuario:
            return False, "Ya estás inscrito en esta aula"
    print(" ")
    nombre=input("Ingresa un nombre y un apellido: ")
    print(" ")
    nuevo_estudiante = {
        "nombre": nombre,
        "Usuario": nombre_de_usuario,
        "tareas_entregadas": []
    }

    datos_aula["estudiantes"].append(nuevo_estudiante)

    with open(archivo, "w", encoding="utf-8") as json_file:
        json.dump(
            datos_aula,
            json_file,
            indent=4,
            ensure_ascii=False
        )

    return True, "Inscripción realizada correctamente"

def validar_estudiante(codigo_aula, nombre_de_usuario):
    valor, resultado=validar_aula(codigo_aula)
    
    if not valor:
        return False, resultado
    
    archivo=resultado
    with open(archivo, "r", encoding="utf-8") as file:
        datos_json=json.load(file)
        
    for estudiante in datos_json["estudiantes"]:
        if estudiante["Usuario"] == nombre_de_usuario:
            return True, "Usuario inscrito"

    print("________________________")
    print("Usuario no esta inscrito")
    print(" ")
    return False, "_"

def entregar_tarea(nombre_de_usuario):
    print(" ")
    codigo_aula=input("Ingresa el codigo de aula: ")
    valor, resultado = validar_estudiante(codigo_aula, nombre_de_usuario)

    if not valor:
        return False, resultado


    archivo = CARPETAS_AULAS / f"aula_{codigo_aula.strip().upper()}.json"

    with open(archivo, "r", encoding="utf-8") as file:
        datos_json = json.load(file)

    # Buscar los datos del estudiante
    estudiante_encontrado = None

    for estudiante in datos_json["estudiantes"]:
        if estudiante["Usuario"] == nombre_de_usuario:
            estudiante_encontrado = estudiante
            break

    if estudiante_encontrado is None:
        return False, "No se encontró al estudiante."

    if not datos_json["tareas"]:
        return False, "No hay tareas disponibles en esta aula."

    print("\n--- TAREAS DISPONIBLES ---")

    for tarea in datos_json["tareas"]:
        print(f"\nID: {tarea['id']}")
        print(f"Título: {tarea['titulo']}")

    id_tarea = input("\nIngresa el ID de la tarea: ").strip()

    tarea_encontrada = None

    for tarea in datos_json["tareas"]:
        if tarea["id"] == id_tarea:
            tarea_encontrada = tarea
            break

    if tarea_encontrada is None:
        return False, "No se encontró esa tarea."

    # 6. Crear la lista de usuarios si todavía no existe
    tarea_encontrada.setdefault("usuarios", [])

    # 7. Evitar que el estudiante entregue dos veces la misma tarea
    for usuario in tarea_encontrada["usuarios"]:
        if usuario["usuario"] == nombre_de_usuario:
            return False, "Ya entregaste esta tarea."

    while True:
        enlace_entrega = input("\nIngresa el enlace de tu entrega: ").strip()

        if not enlace_entrega.startswith(("https://", "http://")):
            print("El enlace no es válido.")
        else:
            break

    
    tarea_encontrada["usuarios"].append({
        "nombre": estudiante_encontrado["nombre"],
        "usuario": estudiante_encontrado["Usuario"],
        "enlace_entrega": enlace_entrega
    })

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos_json, file, indent=4, ensure_ascii=False)

    return True, "Tarea entregada correctamente."

def buscar_tarea_por_id():
    print(" ")
    print("_____BUSCAR TAREAS_____")
    print(" ")
    codigo_aula = input("Ingresa el código del aula: ").strip().upper()
    print(" ")
    archivo = CARPETAS_AULAS / f"aula_{codigo_aula}.json"

    if not archivo.is_file():
        print("El código del aula no existe.")
        return None

    with open(archivo, "r", encoding="utf-8") as file:
        datos_aula = json.load(file)

    if not datos_aula["tareas"]:
        print("__________________________________")
        print("Esta aula todavía no tiene tareas.")
        print(" ")
        return None
    print("___________________")
    id_tarea = input("Ingresa el ID de la tarea: ").strip()
    print(" ")

    for tarea in datos_aula["tareas"]:
        if tarea["id"] == id_tarea:
            print("___________________________________")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Enlace: {tarea['enlace']}")
            print(" ")
            return tarea
    print(" ")
    print("No se encontró una tarea con ese ID.")
    print("____________________________________")
    return None

def mostrar_perfil(usuario):

    ruta_json=obtener_ruta("MIAUla.json")

    with open (ruta_json, "r", encoding="utf-8") as file:
        datos_json=json.load(file)

    print("_____________________________")
    print("__________MI PERFIL__________")
    print(" ")

    print("="*50)
    print(f"Nombre: {datos_json[usuario][0]}")
    print("="*50)
    print(f"Universidad: {datos_json[usuario][1]}")
    print("="*50)
    print(f"Correo electronico: {datos_json[usuario][2]}")

def mostrar_todas_las_tareas():
    codigo_aula=input("Introduce el codigo de el aula: ").strip().upper()

    archivo_aula = CARPETAS_AULAS / f"aula_{codigo_aula}.json"

    if not archivo_aula.exists():
        print("El aula no existe.")
        return

    with open(archivo_aula, "r", encoding="utf-8") as archivo:
        datos_aula = json.load(archivo)

    tareas = datos_aula.get("tareas", [])

    if not tareas:
        print("Esta aula todavía no tiene tareas.")
        return

    print("\n========== TODAS LAS TAREAS ==========")

    for numero, tarea in enumerate(tareas, start=1):
        print(f"\nTarea {numero}")
        print(f"Código: {tarea.get('id', 'Sin código')}")
        print(f"Título: {tarea.get('titulo', 'Sin título')}")
        print(f"Descripción: {tarea.get('descripcion', 'Sin descripción')}")
        print("--------------------------------------")