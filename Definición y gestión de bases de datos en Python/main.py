import sqlite3
import getpass
conn = sqlite3.connect('app.bd')


def secondMain() :
    crearUsuario(222, "brian", 'admin')

def showAll():
    cusor = conn.cursor()
    rows = cusor.execute('SELECT * FROM users')

    for row in rows:
        print(row)

    cusor.close()

    conn.close()


def main():
    showAll()

    username = input('Nombre de usuario :')
    password = getpass.getpass("Contaseña :")
    if verificaCredenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")


def verificaCredenciales(username, password):
    conn = sqlite3.connect('app.bd')
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username = "{username}" AND password = "{password}"'
    print(query)

    row = cursor.execute(query)
    data = row.fetchone()
    print('data es :', type(data))

    cursor.close()
    conn.close()

    if data == None:
        return False
    return True


def crearUsuario(identificador, usuario, clave):
    conn = sqlite3.connect('app.bd')
    cursor = conn.cursor()

    query = f'INSERT INTO users( id, username, password) VALUES ( {identificador}, "{usuario}", "{clave}")'

    rows = cursor.execute(query)
    print('data es :', type(rows))
    
    conn.commit()
    cursor.close()
    conn.close()
    
if (__name__ == '__main__'):
    secondMain()
