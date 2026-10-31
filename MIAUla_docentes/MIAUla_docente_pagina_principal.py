def pagina_principal_docentes(codigo_docente, codigo_de_aula):
    import json
    from MIAUla_docente_funciones_principales import publicar_tarea,todas_las_tareas, obtener_ruta

    ruta_json=obtener_ruta("MIAUla_docentes.json")

    try:
        with open(ruta_json, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
            datos={}
    print("__________BIENVENIDO DOCENTE A LA PAGINA PRINCIPAL DE MIAUla 😄__________")
    print(" ")
    codigo_aula=codigo_de_aula
    print(f"Nombre de docente: {datos[codigo_docente][0]}")
    print(f"Universidad: {datos[codigo_docente][1]}")
    print(" ")

    while True:
    
        print("__________MENU PRINCIPAL__________")
        print(" ")
        print("1. Todas las tareas")
        print("2. Publicar tarea")
        print("3. Cerrar sesion")

        while True:
            try:
                opcion=int(input("Ingresa la opcion: "))
                print(f"Su opcion es {opcion}")
                break
            except:
                print("La opcion debe de ser un numero")

        if opcion==1:
            todas_las_tareas(codigo_aula)
        if opcion==2:
            publicar_tarea(codigo_aula)
        if opcion==3:
            print("Cerrando sesion....")
            break
        if opcion not in (1,2,3):
             print("Solo existen 3 opciones")  