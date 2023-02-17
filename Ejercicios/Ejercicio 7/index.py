class Alumno:
    nombre = ''
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        aprobado = False
        if (self.nota >= 6):
            aprobado = True

        print("Nombre:", self.nombre, "Calificacion:", f"{self.nota}", 'Estatus :', "aprobado" if aprobado else "reprobado")

alumno = Alumno("Brian", 10)
alumno.__str__()