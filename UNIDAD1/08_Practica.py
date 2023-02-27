import pprint

class Usuario:
    def __init__(self,usuario,contrasena,nombre,curp,ciudad,rol="Cliente") -> None:
         self.Usuario=usuario
         self.Contrasena=contrasena
         self.Nombre=nombre
         self.Curp=curp
         self.Ciudad=ciudad
         self.Rol=rol
         
    def __repr__(self) -> str:
        return(f"""
        Usuario: {self.Usuario} 
        Contraseña: {self.Contrasena}
        Nombre: {self.Nombre}
        Curp: {self.Curp}
        Ciudad: {self.Ciudad}
        Rol: {self.Rol}\n""")


admin=Usuario("ADMIN","123","Administrador","BEHI99","Nuevo Laredo","Administrador")
usuarios=[admin]

while True:
    try:
     print("\nMENÚ DE OPCIONES\n 1 - Registro\n 2 - Inicio de sesión\n 3 - Salir")
     opcion = int(input("\nSeleccione una opción: "))
    except Exception:
        print("Opcion no valida\n")
        continue
    if opcion==1: #REGISTRO DE DATOS
        print("\nINGRESE LOS SIGUIENTES DATOS\n")
        miUsuario=Usuario(
        input("Usuario: "),
        input("Contraseña: "),
        input("Nombre: "),
        input("Curp: "),
        input("Ciudad: "))

        for i in usuarios:

            if miUsuario.Curp==i.Curp:
                
                print("\nEL USUARIO YA EXISTE.")
                break
        else:
            usuarios.append(miUsuario)
            print("\n¡REGISTRO EXITOSO!\n")
            
            Resp = int (input("\n¿Desea regresar al menú principal? (1-Sí / 2-No)\n -"))
        if Resp == 2:
            print("\n ======= SESIÓN TERMINADA. =======")
            break
                
    if opcion==2: #INICIO DE SESIÓN
        U=input("Usuario: ")
        C=input("Contraseña: ")
       
        for i in usuarios:
            if i.Usuario==U and i.Contrasena==C:
                if i.Rol =="Administrador":
                    print("\nBienvenido administrador \n\n **Usuarios registrados**")
               
                    for x in usuarios:
                        pprint.pprint(usuarios)

                        break
                else: 

                    print(f" \nBIENVENIDO(A)  {i.Nombre}\n")
                    print(i)
            
            else:
                print("\nDATOS INCORRECTOS")
            
        Resp = int (input("\n¿Desea regresar al menú principal? (1-Sí / 2-No)\n -")) #TERMINAR PROGRAMA
        if Resp == 2:
            print("\n ======= SESIÓN TERMINADA. =======")
            break
        
            
