def cambiar_contraseña():
    import json
    from MIAUla_docentes_inicio_de_sesion import iniciar_sesion
    from MIAUla_docente_funciones_principales import obtener_ruta

    ruta_json=obtener_ruta("MIAUla_docentes.json")
    #Abrimos el json
    try:
        with open(ruta_json, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
        datos={}

    #Funcion para guardar los cambios del json   
    def guardar():
        with open(ruta_json, "w") as file:
            json.dump(datos,file, indent=8, ensure_ascii=False)

    while True:
        codigo_de_docente=input("Ingresa codigo de docente: ")
        print("_________________")
        encontrado=False
        if codigo_de_docente in datos:
            while True:
                contraseña=input("Ingresa contraseña: ")
                print("_______________")

                if contraseña == datos[codigo_de_docente][3]:
                    print("Contraseña correcta")
                    encontrado=True
                    
                    while True:
                        print(f"Bienvenido {datos[codigo_de_docente][0]}")
                        print("_______________________________")

                        nueva_contraseña=input("Ingresa nueva contraseña: ")
                        confirmacion_de_nueva_contraseña=input("Vuelve a introducir tu nueva contraseña: ")

                        if confirmacion_de_nueva_contraseña==nueva_contraseña:
                            print("Contraseña cambiada con exito")
                            print("_____________________________")
                            print("Ya puedes iniciar sesion")
                            print(" ")

                            datos[codigo_de_docente][3]=nueva_contraseña
                            guardar()
                            iniciar_sesion()
                            break
                        else:
                            print("Contraseñas no conciden. Intenta de nuevo")
                            print("_________________________________________")
                else:
                    print("Contraseña incorrecta. Intenta otra vez")
                    print("_______________________________________")
        if not encontrado:
            print(f"Usuario: {codigo_de_docente} no esta registrado")