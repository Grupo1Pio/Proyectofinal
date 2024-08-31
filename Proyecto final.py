import pickle

class SalaCine:
    def __init__(self, filas, columnas):
        """Inicializa una nueva sala de cine con las dimensiones dadas."""
        self.filas = filas
        self.columnas = columnas
        self.sala = [['O' for _ in range(columnas)] for _ in range(filas)]  # 'O' representa un asiento desocupado

    def mostrar_sala(self):
        """Muestra el estado actual de la sala."""
        for fila in self.sala:
            print(' '.join(fila))
    
    def asignar_asiento(self, fila, columna):
        """Asigna un asiento en la sala, si está disponible."""
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            if self.sala[fila][columna] == 'O':
                self.sala[fila][columna] = 'X'  # 'X' representa un asiento ocupado
                print(f"Asiento en fila {fila+1}, columna {columna+1} asignado.")
            else:
                print("El asiento ya está ocupado.")
        else:
            print("Posición fuera de rango.")

    def guardar_sala(self, nombre_archivo):
        """Guarda el estado actual de la sala en un archivo de texto y un archivo binario."""
        with open(nombre_archivo + '.txt', 'w') as f:
            for fila in self.sala:
                f.write(' '.join(fila) + '\n')

        with open(nombre_archivo + '.pkl', 'wb') as f:
            pickle.dump(self, f)
        print(f"Sala guardada en {nombre_archivo}.txt y {nombre_archivo}.pkl.")

    @staticmethod
    def cargar_sala(nombre_archivo):
        """Carga el estado de una sala desde un archivo binario."""
        try:
            with open(nombre_archivo + '.pkl', 'rb') as f:
                sala = pickle.load(f)
            print(f"Sala cargada desde {nombre_archivo}.pkl.")
            return sala
        except FileNotFoundError:
            print("Archivo no encontrado.")
            return None


def menu_principal():
    salas = {}  # Diccionario para almacenar las salas creadas
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear nueva sala")
        print("2. Ver estado de la sala")
        print("3. Asignar asiento")
        print("4. Guardar sala")
        print("5. Cargar sala")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            nombre = input("Ingrese el nombre de la sala: ")
            salas[nombre] = SalaCine(filas, columnas)
            print(f"Sala '{nombre}' creada con éxito.")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la sala a mostrar: ")
            if nombre in salas:
                salas[nombre].mostrar_sala()
            else:
                print("Sala no encontrada.")
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la sala: ")
            if nombre in salas:
                fila = int(input("Ingrese el número de fila: ")) - 1
                columna = int(input("Ingrese el número de columna: ")) - 1
                salas[nombre].asignar_asiento(fila, columna)
            else:
                print("Sala no encontrada.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre de la sala a guardar: ")
            if nombre in salas:
                salas[nombre].guardar_sala(nombre)
            else:
                print("Sala no encontrada.")
        
        elif opcion == '5':
            nombre = input("Ingrese el nombre del archivo de la sala a cargar (sin extensión): ")
            sala = SalaCine.cargar_sala(nombre)
            if sala:
                salas[nombre] = sala
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
