def registro():
    import json
    from MIAUla_inicio_de_sesion import iniciar_sesion
    from MIAUla_funciones_principales import obtener_ruta, limpiar

    print("Bienvenido al registro de nuevos usuarios de MIAUla")
    print("____________________________________________________")

    ruta_json=obtener_ruta("MIAUla.json")
#Bloque para abrir el json
    try:
        with open(ruta_json, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
            datos={}

#Funcion para guardar los cambios del json   
    def guardar():
        with open(ruta_json, "w") as file:
            json.dump(datos,file, indent=8, ensure_ascii=False)

#Bloque de registro
    while True:
        nombre_de_usuario=input("Crea tu nombre de usuario: ")

        if nombre_de_usuario in datos:
            print("Este nombre de usuario ya pertenece a otro usuario. Intenta crear otro nombre de usuario")
            print("________________________________________________________________________________________")
        else:
            print(f"Usuario elegido: {nombre_de_usuario} ")
            print("______________________________________")

            primer_nombre=input("Ingrese su primer nombre: ")
            primer_nombre=limpiar(primer_nombre)
            print(f"Tu primer nombre es {primer_nombre}")
            print("____________________________________")
            
            segundo_nombre=input("Ingrese su segundo nombre: ")
            segundo_nombre=limpiar(segundo_nombre)
            print(f"Tu segundo nombre es {segundo_nombre}")
            print("______________________________________")

            primer_apellido=input("Ingrese su primer apellido: ")
            primer_apellido=limpiar(primer_apellido)
            print(f"Tu primer apellido es {primer_apellido}")
            print("________________________________________")

            segundo_apellido=input("Ingrese su segundo apellido: ")
            segundo_apellido=limpiar(segundo_apellido)
            print(f"Tu segundo apellido es {segundo_apellido}")
            print("__________________________________________")

            nombre_completo=primer_nombre+" "+segundo_nombre+" "+primer_apellido+" "+segundo_apellido
            print(f"Nombre completo: {nombre_completo}")
            print("___________________________________")
        
            institucion=input("Ingresa nombre de tu institucion academica: ")
            institucion=limpiar(institucion)
            print(f"Institucion Academica: {institucion}")
            print("_____________________________________")
            
            while True:
                buscar=False
                correo=input("Ingresa tu correo electronico: ")
                for usuario in datos.values():
                    if correo == usuario[2]:
                        buscar=True
                if buscar==True:
                    print("Este correo ya fue registrado. Intenta con otro")
                    print("_______________________________________________")
                else:
                    print("Correo registrado exitosamente")
                    print("______________________________")
                    break

            while True:
                contraseña=input("Ingresa nueva contraseña: ")
                confirmacion=input("Ingresa nuevamente tu contraseña: ")
                if confirmacion == contraseña:
                    print("Coincidencia Exitosa")
                    print("____________________")
                    print(f"Bienvenido {nombre_de_usuario} a MIAUla")
                    break
                else:
                    print("Contraseñas no coinciden. Intenta de nuevo")
                    print("__________________________________________")
            datos[nombre_de_usuario]=[nombre_completo, 
                                        institucion,
                                        correo,
                                        contraseña]
            guardar()
            print("_________________________________________")
            iniciar_sesion()