import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        """
        Prueba la creación de una instancia de Persona.
        """
        persona = Persona("Carlos", "Gutiérrez", "87654321")
        self.assertEqual(persona.nombre, "Carlos")
        self.assertEqual(persona.apellido, "Gutiérrez")
        self.assertEqual(persona.dni, "87654321")

    def test_repr_persona(self):
        """
        Prueba la representación en cadena de una instancia de Persona.
        """
        persona = Persona("Carlos", "Gutiérrez", "87654321")
        esperado = "Persona: DNI: 87654321 Nombre: Carlos Apellido: Gutiérrez Última Idea: <sin ideas por ahora>"
        self.assertEqual(str(persona), esperado)

if __name__ == "__main__":
    unittest.main()
