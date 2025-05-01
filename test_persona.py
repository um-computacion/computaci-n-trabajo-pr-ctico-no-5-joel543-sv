import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_creacion_con_valores_vacios(self):
        """Verifica el comportamiento al instanciar Persona con valores vacíos."""
        persona = Persona("", "", "")
        self.assertEqual(persona.nombre, "")
        self.assertEqual(persona.apellido, "")
        self.assertEqual(persona.dni, "")

    def test_creacion_con_None(self):
        """Verifica la respuesta cuando se pasan valores None."""
        persona = Persona(None, None, None)
        self.assertIsNone(persona.nombre)
        self.assertIsNone(persona.apellido)
        self.assertIsNone(persona.dni)

    def test_pensar_actualiza_contador(self):
        """Comprueba que la cantidad de pensamientos se incrementa correctamente."""
        persona = Persona("Carlos", "Molina", "78945612")
        persona.pensar("Reflexionar sobre la vida")
        self.assertEqual(persona.pensamientos, 1)

if __name__ == "__main__":
    unittest.main()
