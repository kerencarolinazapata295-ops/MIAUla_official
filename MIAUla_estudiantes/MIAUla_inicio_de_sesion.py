def iniciar_sesion():
    import json
    from MIAUla_pagina_principal import pagina_principal
    from MIAUla_funciones_principales import obtener_ruta

    ruta_json=obtener_ruta("MIAUla.json")
    try:
        with open(ruta_json, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
            datos={}

    while True:
        print("____________________________________")
        print("__________Inicio de sesion__________")
        
        nombre_de_usuario_de_inicio_de_sesion=input("Ingrese nombre de usuario: ")
        print("_________________________________________________________________")
        nombre_de_usuario_de_inicio_de_sesion=nombre_de_usuario_de_inicio_de_sesion.strip()

        encontrado=False

        if nombre_de_usuario_de_inicio_de_sesion in datos:
            print(f"Bienvenido {nombre_de_usuario_de_inicio_de_sesion}")
            print("___________________________________________________")

            while True:
                contraseña=input("Ingresa contraseña: ")

                if contraseña == datos[nombre_de_usuario_de_inicio_de_sesion][3]:
                    print("Contraseña correcta")
                    print("___________________")
                    encontrado=True
                    print(f"Bienvenido {datos[nombre_de_usuario_de_inicio_de_sesion][0]} a MIAUla")
                    pagina_principal(nombre_de_usuario_de_inicio_de_sesion)
        
                else:
                    print("Contraseña incorrecta. Intenta otra vez")
                break

        if not encontrado:
            print(f"Codigo unico: {nombre_de_usuario_de_inicio_de_sesion} no esta registrado")