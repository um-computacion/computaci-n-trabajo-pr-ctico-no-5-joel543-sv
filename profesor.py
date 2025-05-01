from src.persona import Persona

class Profesor(Persona):
    """Representa a un profesor, heredando de Persona."""

    def __init__(self, nombre, apellido, dni, sueldo):
        """
        Inicializa un Profesor con validaciones de sueldo.

        Args:
            nombre (str): Nombre del profesor.
            apellido (str): Apellido del profesor.
            dni (str): Número de identificación único.
            sueldo (float): Salario del profesor.

        Raises:
            ValueError: Si el sueldo es negativo.
        """
        if sueldo < 0:
            raise ValueError("El sueldo no puede ser negativo.")
        super().__init__(nombre, apellido, dni)
        self.sueldo = sueldo

    def __repr__(self):
        """
        Retorna una representación en cadena de la instancia.

        Returns:
            str: Información del profesor con su sueldo.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
