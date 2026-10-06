import sqlite3


conexion = sqlite3.connect("universidad.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    carrera TEXT
)
""")

conexion.commit()



def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")


def registrar_estudiante():
    nombre = input("Nombre: ")
    edad = pedir_numero("Edad: ")
    carrera = input("Carrera: ")

    cursor.execute("""
    INSERT INTO estudiantes (nombre, edad, carrera)
    VALUES (?, ?, ?)
    """, (nombre, edad, carrera))

    conexion.commit()

    print("Estudiante registrado correctamente.")


def ver_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    print("\n===== ESTUDIANTES =====")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print(
                f"ID: {estudiante[0]} | "
                f"{estudiante[1]} | "
                f"{estudiante[2]} años | "
                f"{estudiante[3]}"
            )

def actualizar_estudiante():
    id_estudiante = pedir_numero("ID del estudiante: ")

    nombre = input("Nuevo nombre: ")
    edad = pedir_numero("Nueva edad: ")
    carrera = input("Nueva carrera: ")

    cursor.execute("""
    UPDATE estudiantes
    SET nombre = ?, edad = ?, carrera = ?
    WHERE id = ?
    """, (nombre, edad, carrera, id_estudiante))

    conexion.commit()

    if cursor.rowcount > 0:
        print("Estudiante actualizado correctamente.")
    else:
        print("No se encontró un estudiante con ese ID.")



def eliminar_estudiante():
    id_estudiante = pedir_numero(
        "ID del estudiante a eliminar: "
    )

    cursor.execute("""
    DELETE FROM estudiantes
    WHERE id = ?
    """, (id_estudiante,))

    conexion.commit()

    if cursor.rowcount > 0:
        print("Estudiante eliminado correctamente.")
    else:
        print("No se encontró un estudiante con ese ID.")


while True:
    print("\n===== UNIVERSIDAD =====")
    print("1. Registrar estudiante")
    print("2. Ver estudiantes")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()

    elif opcion == "2":
        ver_estudiantes()

    elif opcion == "3":
        actualizar_estudiante()

    elif opcion == "4":
        eliminar_estudiante()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
