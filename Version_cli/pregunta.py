import respuesta

class Pregunta():
    def __init__(self, id, cuerpo, dificultad=0, tematica='general') -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__dificultad = dificultad
        self.__tematica = tematica
        self.__respuestas =[] #Colección de objetos Respuesta
        self.__correcta = None

    def asigna_respuestas(self, col_respuestas):
        self.__respuestas = col_respuestas
        for c in col_respuestas:
            if c.correcta:
                self.__correcta = c.id
                break
    def get_resp_correcta(self):
        for r in self.__respuestas:
            if r.correcta:
                return r.cuerpo
    @property
    def respuestas(self):
        return self.__respuestas

    @property
    def id(self):
        return self.__id

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def dificultad(self):
        return self.__dificultad
            
    @property
    def tematica(self):
        return self.__tematica 

    @property
    def correcta(self):
        return self.__correcta

