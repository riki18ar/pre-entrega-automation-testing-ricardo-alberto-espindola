# Exporta todas las funciones y clases definidas en este paquete.


class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad


    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")



# Creando el objeto de la clase Persona instanciando la clase
personaNumeroUno = Persona("Ana", 30)
personaNumeroDos = Persona("Luis", 25)

personaNumeroDos.cumplir_anios()