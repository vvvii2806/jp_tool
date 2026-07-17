from app.backend.connect import *

def limpiar_tablas_de_prueba():
    cursor, connection = create_cursor()
    
    cursor.execute("TRUNCATE TABLE words RESTART IDENTITY CASCADE;")
    connection.commit()
    

    close_connection(cursor, connection)
    print("DB clean")

if __name__ == "__main__":
    limpiar_tablas_de_prueba()