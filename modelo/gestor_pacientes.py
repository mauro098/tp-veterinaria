from paciente import Paciente

class GestorPacientes:
    def __init__(self):
        self.__pacientes = []

    def insertar(self, paciente):
        for p in self.__pacientes:
            if p.codigo == paciente.codigo:
                return False
        self.__pacientes.append(paciente)
        return True

    def mostrar_todos(self):
        if len(self.__pacientes) == 0:
            print("No hay pacientes")
        else:
            for p in self.__pacientes:
                print(f"Código: {p.codigo}, Nombre: {p.nombre}, Dueño: {p.dueno}, Especie: {p.especie}, Raza: {p.raza}")
   
    def buscar_por_codigo(self, codigo):
        comparaciones = 0
        for p in self.__pacientes:
            comparaciones += 1
            if p.codigo == codigo:
                return p, comparaciones
        return None, comparaciones
    
    def buscar_por_nombre(self, nombre):
        for p in self.__pacientes:
            if p.nombre == nombre:
                return p
        return None
    
    def buscar_por_dueno(self, dueno):
        for p in self.__pacientes:
            if p.dueno == dueno:
                return p
        return None
    
    def buscar_por_especie(self, especie):
        for p in self.__pacientes:
            if p.especie == especie:
                return p
        return None
    
    def buscar_por_raza(self, raza):
        for p in self.__pacientes:
            if p.raza == raza:
                return p
        return None


if __name__ == "__main__":
    gestor = GestorPacientes()
    print(gestor.insertar(Paciente(1, "Firulais", "Perro", "Caniche", 4, "Laura Gómez")))
    print(gestor.insertar(Paciente(2, "Michi", "Gato", "Siamés", 2, "Carlos Pérez")))
    print(gestor.insertar(Paciente(1, "Rex", "Perro", "Ovejero", 6, "Ana Díaz")))
    gestor.mostrar_todos()