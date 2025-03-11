# SISTEMA DE GESTIÓN DE BIBLIOTECA
# Este programa permite administrar una biblioteca mediante un menú interactivo, gestionado desde la consola.
# Se desarrollo implementando la Programación Orientada a Objetos (POO).

# Funcionalidades:
# - Agregar libros
# - Prestar libros
# - Devolver libros
# - Mostrar todos los libros
# - Buscar libros por ISBN

class Libro: # Clase que representa un libro en la biblioteca.
    
    """Se declaran las variables y se define el tipo de datos que se viculara con las mismas."""
    def __init__(self, gs_titulo: str, gs_autor: str, gs_isbn: str): 
        """Inicializa un libro con título, autor, ISBN y estado disponible."""
        self.titulo = gs_titulo.title()
        self.autor = gs_autor.title()
        self.isbn = gs_isbn
        self.is_disponible = True  # Por defecto, un libro nuevo está disponible
    
    def prestar(self):
        """Cambia el estado del libro a 'No disponible' si está disponible."""
        if self.is_disponible:
            self.is_disponible = False
       #se hace uso de f'' (f-string) para formatear cadenas, sin la necesidad de usar la expresion format() o concatenaciones usando +  
            print(f'📕 El libro "{self.titulo}" ha sido prestado.') 
        else:
            print(f'❌ El libro "{self.titulo}" ya está prestado.')
    
    def devolver(self):
        """Cambia el estado del libro a 'Disponible' si estaba prestado."""
        if not self.is_disponible:
            self.is_disponible = True
            print(f'📗 El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'❌ El libro "{self.titulo}" ya estaba disponible.')

    def mostrar_info(self):
        """Muestra la información del libro y su estado actual."""
        estado = "Sí" if self.is_disponible else "No"
        return f'{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'

class Biblioteca:
    """Clase que gestiona la colección de libros de la biblioteca."""
    
    def __init__(self):
        """Inicializa una biblioteca vacía."""
        self.libros = []
    
    def agregar(self, titulo, autor, isbn):
        """Agrega un nuevo libro a la biblioteca."""
        nuevo_libro = Libro(titulo, autor, isbn)
        self.libros.append(nuevo_libro)
        print(f'📖 El libro "{titulo}" ha sido agregado con éxito.')
    
    def mostrar(self):
        """Muestra todos los libros en la biblioteca."""
        if not self.libros:
            print("📚 La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(libro.mostrar_info())
    
    def buscar(self, isbn):
        """Busca un libro por su ISBN y muestra su información."""
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro.mostrar_info())
                return libro
        print("❌ No se encontró ningún libro con ese ISBN.")
        return None
    
    def prestar(self, isbn):
        """Busca un libro por ISBN y lo presta si está disponible."""
        libro = self.buscar(isbn)
        if libro:
            libro.prestar()
    
    def devolver(self, isbn):
        """Busca un libro por ISBN y lo devuelve si estaba prestado."""
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()

def menu():
    """Función que muestra el menú y permite al usuario interactuar con la biblioteca."""
    biblioteca = Biblioteca()
    while True:
        print("\n📌 Menú de la Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro por ISBN")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            biblioteca.agregar(titulo, autor, isbn)
        elif opcion == "2":
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            biblioteca.prestar(isbn)
        elif opcion == "3":
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            biblioteca.devolver(isbn)
        elif opcion == "4":
            biblioteca.mostrar()
        elif opcion == "5":
            isbn = input("Ingresa el ISBN a buscar: ")
            biblioteca.buscar(isbn)
        elif opcion == "6":
            print("📕 Saliendo del sistema de gestión de biblioteca...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
