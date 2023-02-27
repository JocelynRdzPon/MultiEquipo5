"""
#8 Resumen y multi-solución 
8.1.-Definir una clase usuario que contenga como atributos: 
Usuario 
Contraseña 
Rol 
Nombre 
CURP 
Ciudad 
"""
import pprint

class Usuario:
    def __init__(self,usuario,contrasena,rol,nombre,curp,ciudad) -> None:
         self.Usuario=usuario
         self.Contrasena=contrasena
         self.Rol=rol
         self.Nombre=nombre
         self.Curp=curp
         self.Ciudad=ciudad
         
    def __repr__(self) -> str:
        return(f"""
        Usuario:{self.Usuario} 
        Contraseña:{self.Contrasena}
        Rol:{self.Rol}
        Nombre:{self.Nombre}
        Curp:{self.Curp}
        Ciudad:{self.Ciudad}\n""")



"""8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la 
información de todos los usuarios registrados al momento."""
admin=Usuario("ADMIN","123","Administrador","Administrador","BEHI991105","Nuevo Laredo")
usuarios=[admin]


"""8.2.-Realizar un programa que contenga el siguiente menú 
1.- Registro 
2.- Inicio de sesión 
3.- Salida 
"""
while True:
    try:
     print("\nMENÚ DE OPCIONES\n 1 - Registro\n 2 - Inicio de sesión\n 3 - Salir")
     opcion = int(input("\nSeleccione una opción: "))
    except Exception:
        print("Opcion no valida\n")
        continue
    if opcion==1:
        print("\nINGRESE LOS SIGUIENTES DATOS\n")
        miUsuario=Usuario(
        input("Usuario: "),
        input("Contraseña: "),
        input("Rol:"),
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
                
    if opcion==2:
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
            
        Resp = int (input("\n¿Desea regresar al menú principal? (1-Sí / 2-No)\n -"))
        if Resp == 2:
            print("\n ======= SESIÓN TERMINADA. =======")
            break