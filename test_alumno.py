import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        """
        Verifica que se cree correctamente un alumno con los atributos adecuados.
        """
        alumno = Alumno("Mateo", "Fernández", "98765432", "B456")
        self.assertEqual(alumno.nombre, "Mateo")
        self.assertEqual(alumno.apellido, "Fernández")
        self.assertEqual(alumno.dni, "98765432")
        self.assertEqual(alumno.legajo, "B456")

    def test_repr_alumno(self):
        """
        Prueba la representación en cadena de un Alumno.
        """
        alumno = Alumno("Mateo", "Fernández", "98765432", "B456")
        esperado = "Alumno: DNI: 98765432 Nombre: Mateo Apellido: Fernández Legajo: B456"
        self.assertEqual(str(alumno), esperado)

if __name__ == "__main__":
    unittest.main()
