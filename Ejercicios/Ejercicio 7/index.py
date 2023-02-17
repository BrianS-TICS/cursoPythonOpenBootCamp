class Alumno:
    nombre = ''
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        aprovado = False
        if (aprovado >= 6):
            aprovado = True

        print("Nombre:", self.nombre, "Calificacion:", f"{self.nota}")

alumno = Alumno("Brian", 10)
alumno.__str__()