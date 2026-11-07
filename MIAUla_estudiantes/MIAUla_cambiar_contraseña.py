def cambiar_contraseña():
    import json
    from MIAUla_inicio_de_sesion import iniciar_sesion
    from MIAUla_funciones_principales import obtener_ruta, generar_codigo, limpiar

    ruta_json=obtener_ruta("MIAUla.json")
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
        nombre_de_usuario=input("Ingresa nombre de usuario: ")
        print("_________________")
        encontrado=False
        if nombre_de_usuario in datos:
            encontrado=True
            posicion=datos.get(nombre_de_usuario)
            correo=input("Ingresa correo electronico: ")
            if correo == posicion[2]:
                codigo_generado=generar_codigo()
                print(f"\ncodigo generado: {codigo_generado}")
                ingresa_codigo=input(f"\nIngresa el codigo enviado al correo electronico: {correo}: ").upper()
                if ingresa_codigo==codigo_generado:
                    print("\nCodigo correcto")
                    nueva_contraseña=input("\nIngresa tu nueva contraseña: ")
                    confirmar_contraseña=input("\nIngresa nuevamente tu contraseña: ")
                    if nueva_contraseña==confirmar_contraseña:
                        datos[nombre_de_usuario][3]=confirmar_contraseña
                        print("\nTu contraseña ha sido cambiada con exito ✅")
                        guardar()
                        break
                    else:
                        print("\nContraseñas no coinciden. Intentalo de nuevo")
                else:
                    print("Codigo incorrecto revisa tu correo")
        if not encontrado:
            print("Este usuario no fue encontrado")