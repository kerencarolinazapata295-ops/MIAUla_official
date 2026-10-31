def iniciar_sesion():
    import json
    from MIAUla_docente_pagina_principal import pagina_principal_docentes
    from MIAUla_docente_funciones_principales import obtener_ruta

    ruta_json=obtener_ruta("MIAUla_docentes.json")
    try:
        with open(ruta_json, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
            datos={}

    while True:
        print("____________________________________")
        print("__________Inicio de sesion__________")
        print(" ")
        
        codigo_de_docente_de_inicio_de_sesion=input("Ingrese codigo de docente: ").strip().upper()
        print("_________________________________________________________________")

        encontrado=False

        if codigo_de_docente_de_inicio_de_sesion in datos:
            print(f"Bienvenido {datos[codigo_de_docente_de_inicio_de_sesion][0]}") 
            print("___________________________________________________")

            while True:
                contraseña=input("Ingresa contraseña: ")

                if contraseña == datos[codigo_de_docente_de_inicio_de_sesion][3]:
                    print("Contraseña correcta")
                    print("___________________")
                    encontrado=True
                    codigo_de_aula=datos[codigo_de_docente_de_inicio_de_sesion][4]
                    pagina_principal_docentes(codigo_de_docente_de_inicio_de_sesion, codigo_de_aula)
                    break

                else:
                    print("Contraseña incorrecta. Intenta otra vez 👮")
                break

        if not encontrado:
            print(f"Codigo de docente: {codigo_de_docente_de_inicio_de_sesion} no esta registrado o no ha sido aceptado por la oficina de registro")