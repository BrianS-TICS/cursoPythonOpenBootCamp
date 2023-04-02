import sqlite3


def connectBd(query):
    conn = sqlite3.connect('app.bd')
    cursor = conn.cursor()

    rows = cursor.execute(query)
    data = rows.fetchall()

    cursor.close()
    conn.commit()
    conn.close()

    return data


def request(query):
    data = connectBd(query)
    print(data)


def main():

    request('INSERT INTO Alumnos VALUES (1, "Brian", "Sanchez")')
    request('INSERT INTO Alumnos VALUES (2, "Jose", "Perez")')
    request('INSERT INTO Alumnos VALUES (3, "Diego", "Maradona")')
    request('INSERT INTO Alumnos VALUES (4, "Arnold", "Schema")')
    request('INSERT INTO Alumnos VALUES (5, "Sonia", "Maldonado")')
    request('INSERT INTO Alumnos VALUES (6, "Francisca", "Ochoa")')
    request('INSERT INTO Alumnos VALUES (7, "Francisco", "Javier")')
    request('INSERT INTO Alumnos VALUES (8, "Manuel", "Obrador")')

    print('CONSOLTA DE ALUMNOS')
    nombre = input('Consulta un nombre')
    request(f'SELECT * FROM Alumnos WHERE( nombre = "{nombre}")')


if (__name__ == '__main__'):
    main()
