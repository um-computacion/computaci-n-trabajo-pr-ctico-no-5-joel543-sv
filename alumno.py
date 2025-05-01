from src.persona import Persona

class Alumno(Persona):
    """
    Representa a un alumno, heredando de Persona.
    """

    def __init__(self, nombre, apellido, dni, legajo):
        """
        Inicializa una instancia de Alumno.

        Parámetros:
            nombre (str): Nombre del alumno.
            apellido (str): Apellido del alumno.
            dni (str): Número de identificación único.
            legajo (str): Código de legajo del alumno.
        """
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def __repr__(self):
        """
        Retorna una representación en cadena de la instancia.

        Retorna:
            str: Información del alumno con su legajo.
        """
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"
