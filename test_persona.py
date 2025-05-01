import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_pensar_incrementa_contador(self):
        """
        Prueba que el contador de pensamientos se incremente al registrar una idea.
        """
        persona = Persona("Luis", "Ramírez", "98765432")
        persona.pensar("Aprender programación")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        """
        Prueba que la última idea registrada sea la correcta.
        """
        persona = Persona("Luis", "Ramírez", "98765432")
        persona.pensar("Aprender programación")
        self.assertEqual(persona.ultima_idea, "Aprender programación")

if __name__ == "__main__":
    unittest.main()
