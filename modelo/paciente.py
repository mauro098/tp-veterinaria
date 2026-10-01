class Paciente:
    def __init__(self, codigo, nombre, especie, raza, edad, dueno):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__dueno = dueno

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Dueño: {self.dueno}, Especie: {self.especie}, Raza: {self.raza}"

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_dueno(self):
        return self.__dueno

    def set_dueno(self, dueno):
        self.__dueno = dueno

    codigo = property(get_codigo, set_codigo)
    nombre = property(get_nombre, set_nombre)
    especie = property(get_especie, set_especie)
    raza = property(get_raza, set_raza)
    edad = property(get_edad, set_edad)
    dueno = property(get_dueno, set_dueno)
