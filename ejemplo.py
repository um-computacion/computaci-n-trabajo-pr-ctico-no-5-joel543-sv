from src.alumno import Alumno
from src.profesor import Profesor

# Creación de instancias
profesor1 = Profesor("Marcos", "Gómez", "12345678", 90000)
alumno1 = Alumno("Elena", "Rodríguez", "87654321", "C789")

# Mostrar información
print(profesor1)
print(alumno1)

# Ejemplo de interacción: el alumno piensa en un tema de clase
alumno1.pensar("Estudiar teoría de algoritmos")
print(alumno1)
