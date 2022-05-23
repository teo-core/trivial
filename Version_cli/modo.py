class Modo():
    def __init__(self, 
                nombre = 'Básico',
                tmax_juego= 600, 
                tmax_pregunta=60, 
                num_preguntas=10, 
                num_jugadores=1) -> None:
    
        self.__nombre = nombre
        self.__tmax_juego    = tmax_juego
        self.__tmax_pregunta = tmax_pregunta
        self.__num_preguntas = num_preguntas
        self.__num_jugadores = num_jugadores

    @property
    def tmax_juego(self):
        return self.__tmax_juego

    @property
    def tmax_pregunta(self):
        return self.__tmax_pregunta

    @property
    def num_preguntas(self):
        return self.__num_preguntas
    
    @property
    def num_jugadores(self):
        return self.__num_jugadores    
    
    @property
    def nombre(self):
        return self.__nombre