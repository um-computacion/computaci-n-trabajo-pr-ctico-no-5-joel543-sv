import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        """
        Verifica que se cree correctamente un profesor con los atributos adecuados.
        """
        profesor = Profesor("María", "López", "87654321", 75000)
        self.assertEqual(profesor.nombre, "María")
        self.assertEqual(profesor.apellido, "López")
        self.assertEqual(profesor.dni, "87654321")
        self.assertEqual(profesor.sueldo, 75000)

    def test_repr_profesor(self):
        """
        Prueba la representación en cadena de un Profesor.
        """
        profesor = Profesor("María", "López", "87654321", 75000)
        esperado = "Profesor: DNI: 87654321 Nombre: María Apellido: López Sueldo: 75000"
        self.assertEqual(str(profesor), esperado)

if __name__ == "__main__":
    unittest.main()
