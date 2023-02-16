# CLASES Y OBJETOS
class Empleado:
    name = ""
    trabajando = False

    def getData(self):
        print("Tabajando : ", self.trabajando, " Nombre ", self.name)


empleado = Empleado()
empleado.getData()
