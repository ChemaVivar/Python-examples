from pywebio.input import *
from pywebio.output import *


put_text("Bienvenido a la encuesta de Frameworks Python")
def secuenciallenar():


            nombre = input("Escriba su nombre")
            apellido = input("Escriba su apellido")
            edad = input("Escriba su edad",
            type = NUMBER)
            conocefw = checkbox("Conoce los framework Streamlit y PywebIO?",
            options = [("si"), ("no")])
            frameprefer = select("Seleccione su Framework de preferencia",
            ["Django", "Flask", "Streamlit", "PywebIO"])
            put_table([
            ["Nombre", "Apellido", "Edad", "Conoce Framework", "Framework favorito"],
            [nombre, apellido, edad, conocefw, frameprefer]
            ])


opcion = ["si"]
while opcion == ["si"]:
       secuenciallenar()
       opcion = checkbox("Desea agregar usuario?", options=["si", "no"])
else:
    pass
    
    popup('Gracias', 'Muchas gracias por colaborar') 
