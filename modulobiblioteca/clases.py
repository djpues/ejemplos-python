class Persona:
    def __init__(self, nombre=""):
        self.nombre = nombre
    def __str__(self):
        return "Persona[nombre: "+self.nombre+"]"