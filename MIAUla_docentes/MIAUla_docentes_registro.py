def docente_registro():
    import json
    from MIAUla_docente_funciones_principales import obtener_ruta
    def limpiar(x):
        return " ".join ((x).strip().lower().split()).title()

    ruta_json_pendientes=obtener_ruta("MIAUla_docentes_pendientes.json")

    print(" ")
    print("Bienvenido al registro de docentes de MIAUla")
    print("____________________________________________________")

#Bloque para abrir el json
    try:
        with open(ruta_json_pendientes, "r") as file:
            datos=json.load(file)
    except FileNotFoundError:
            datos={}

#Funcion para guardar los cambios del json   
    def guardar():
        with open(ruta_json_pendientes, "w") as file:
            json.dump(datos,file, indent=8, ensure_ascii=False)

#Bloque de registro
    while True:
        numero=1
        while f"XXX{numero}" in datos:
            numero+=1
        
        codigo_de_docente=(f"XXX{numero}")
        print("_"*20)
        print(f"Tu codigo temporal es: {codigo_de_docente}\n Acercate a la oficina de registro de la universidad para entregar el codigo y ser aceptado en el programa de docentes ⚠️")
        print("_"*20)

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
                print(f"Bienvenido {nombre_completo} a MIAUla")
                break
            else:
                print("Contraseñas no coinciden. Intenta de nuevo")
                print("__________________________________________")
        datos[codigo_de_docente]=[nombre_completo, 
                                        institucion,
                                        correo,
                                        contraseña]
        guardar()
        print("Te recordamos llevar tu codigo temporal a la oficina de registro para asi ser aceptado en el programa y otorgarte tu codigo de docente ⚠️")
        print(f"Codigo temporal:{codigo_de_docente}")
        break