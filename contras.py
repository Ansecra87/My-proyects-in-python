import random

caracteres = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0123456789!@#~½¬{[]}!"
contraseña = "".join(random.choices(caracteres, k= 8 ))
useryes = input("¿Generar contraseña aleatoria?: ").lower()
longitud = int(input ("¿Cuantos caracteres quieres?: "))
contraseña = "".join(random.choices(caracteres, k= longitud ))

if useryes in ["si", "yes", "ok"]:
    print(contraseña)
elif useryes == "no":
    print("Saliendo del generador...")
else:
    print("Opcion no válida")

try:
    longitud = int(input ("¿Cuantos caracteres quieres?: "))
except ValueError:
    print("Debes ingresar un número.")
exit()