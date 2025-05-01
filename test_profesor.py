import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_sueldo_negativo(self):
        """Prueba que un sueldo negativo genere un error."""
        with self.assertRaises(ValueError):
            Profesor("Luisa", "Martínez", "65432178", -50000)

    def test_formato_dni(self):
        """Verifica que el DNI sea válido (solo números)."""
        profesor = Profesor("Luisa", "Martínez", "65432178", 70000)
        self.assertTrue(profesor.dni.isdigit())

if __name__ == "__main__":
    unittest.main()
