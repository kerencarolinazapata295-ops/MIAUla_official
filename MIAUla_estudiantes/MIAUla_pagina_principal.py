def pagina_principal(usuario):
        from MIAUla_funciones_principales import inscribir_estudiante, entregar_tarea, buscar_tarea_por_id, mostrar_perfil, obtener_ruta, mostrar_todas_las_tareas, menu_de_inicio, pedir_opcion
        import json

        ruta_json=obtener_ruta("MIAUla.json")
        try:
            with open(ruta_json, "r") as file:
                datos=json.load(file)
        except FileNotFoundError:
                datos={}
        print(f"Nombre de estudiante: {datos[usuario][0]}")
        print(f"Universidad: {datos[usuario][1]}")

        while True:
            menu_de_inicio()
            opcion=pedir_opcion()
        
            if opcion==1:
                entregar_tarea(usuario)
            if opcion==2:
                buscar_tarea_por_id()
            if opcion==3:
                inscribir_estudiante(usuario)
            if opcion==4:
                mostrar_perfil(usuario)
            if opcion==5:
                mostrar_todas_las_tareas()
            if opcion==6:
                break
            if opcion not in(1,2,3,4,5,6):
                 print("Solo existen 6 opciones. Intenta de nuevo")