import sqlite3
 
class DataBase
    open("database.db", "w").close() # Crear el archivo
 
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
 
    # Crear una tabla
    cursor.execute("CREATE TABLE tabla (entero INT, texto TEXT)")
 
    def commit(self):
    # Guardar
    conn.commit()