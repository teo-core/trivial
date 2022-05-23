from random import shuffle
from settings import BD
from sql import Sql
from pregunta import Pregunta
from respuesta import Respuesta

class Partida():
    def __init__(self, obj_jugador, obj_modo,col_preguntas=None) -> None:
        self.__jugador = obj_jugador
        self.__modo = obj_modo
        self.__col_preguntas = col_preguntas
        self.__marcador = 0 

    @property
    def preguntas(self):
        return self.__col_preguntas[0:self.__modo.num_preguntas]

    @property
    def marcador(self):
        return self.__marcador

    def iniciar(self):
        if not self.__col_preguntas:
            self.__cargar_preguntas()

    def finalizar(self):
        pass

    def barajar(self):
        shuffle(self.__col_preguntas)

    def comprobar_resp(self, obj_pregunta, usr_respuesta):
        if obj_pregunta.correcta == usr_respuesta:
            return 1
        else:
            return 0
    
    def __cargar_preguntas(self):
        lista_preguntas = []
        lista_resp = []
        mi_sql = Sql(BD)
        todas_preg = mi_sql.select('select id, cuerpo, dificultad, tematica from preguntas')
        for tp in todas_preg:
            nueva_preg = Pregunta(tp[0],tp[1],tp[2],tp[3])
            mis_respuestas = mi_sql.select(f'select id,cuerpo,correcta from respuestas where id_pregunta ={tp[0]}')
            for mr in mis_respuestas:
                nueva_resp = Respuesta(mr[0],mr[1],mr[2])
                lista_resp.append(nueva_resp)

            nueva_preg.asigna_respuestas(lista_resp.copy())
            lista_preguntas.append(nueva_preg)
            lista_resp.clear()
        self.__col_preguntas = lista_preguntas
        




