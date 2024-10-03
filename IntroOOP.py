# Definición de la clase Persona
class Persona:
    # Atributo de clase
    especie = "Humano"

    # Método constructor (inicializador)
    def __init__(self, nombre, edad, ocupacion):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    # Método de instancia: Saludar
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    # Método de instancia: Cambiar ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    # Método de instancia: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido años y ahora tiene {self.edad}.")

    # Método de clase: Mostrar la especie
    @classmethod
    def mostrar_especie(cls):
        print(f"Todos pertenecemos a la especie: {cls.especie}.")

    # Método estático: Decir algo genérico
    @staticmethod
    def decir_algo():
        print("Este es un mensaje genérico que no depende de ningún objeto en particular.")

    # Metodo pasar saludo
    def saludarA(self, nombreotrapersona):
        return f"Hola,¨{self.nombre}, Te manda a saludar ¨{nombreotrapersona}"



# Creación de una instancia de la clase Persona
persona1 = Persona("Carlos", 30, "Ingeniero")

# Usar los métodos de la instancia
persona1.saludar()  # "Hola, me llamo Carlos y tengo 30 años."
persona1.cambiar_ocupacion("Doctor")  # "Carlos ahora trabaja como Doctor."
persona1.cumplir_anios()  # "Carlos ha cumplido años y ahora tiene 31."

# Usar el método de clase
Persona.mostrar_especie()  # "Todos pertenecemos a la especie: Humano."

# Usar el método estático
Persona.decir_algo()  # "Este es un mensaje genérico que no depende de ningún objeto en particular."

persona2 = Persona("Alan", 28, "Mecanico")
persona2.saludar()  # "Hola, me llamo Alan y tengo 28 años."
persona2.cambiar_ocupacion("Doctor")  # "Alan ahora trabaja como Maestro."
persona2.cumplir_anios()  # "Carlos ha cumplido años y ahora tiene 29."


persona3 = Persona("Edgar", 32, "Actor")
persona3.saludar()  # "Hola, me llamo Edgar y tengo 32 años."
persona3.cambiar_ocupacion("Doctor")  # "Alan ahora trabaja como director."
persona3.cumplir_anios()  # "Carlos ha cumplido años y ahora tiene 33."

Print()