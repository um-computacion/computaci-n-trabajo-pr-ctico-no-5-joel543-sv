class Persona:
    """
    Representa a una persona con información básica y capacidad de pensamiento.
    """

    def __init__(self, nombre, apellido, dni):
        """
        Inicializa una instancia de Persona.

        Parámetros:
            nombre (str): Primer nombre de la persona.
            apellido (str): Apellido de la persona.
            dni (str): Número de identificación único.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<sin ideas aún>"

    def pensar(self, idea):
        """
        Registra un pensamiento en la persona.

        Parámetros:
            idea (str): Descripción de la idea pensada.
        """
        self.pensamientos += 1
        self.ultima_idea = idea

    def __repr__(self):
        """
        Retorna una representación en cadena de la instancia.

        Retorna:
            str: Información de la persona con su último pensamiento.
        """
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Última Idea: {self.ultima_idea}"
