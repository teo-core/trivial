import os
from partida import Partida
from jugador import Jugador
from modo import Modo
from settings import NUM_PREGUNTAS

def borrar_pantalla():
    os.system('clear')

def get_entrada(opciones):
    while True:
        try:
            entrada = int(input('\nIntroduzca el número de la respuesta: '))
        except Exception:
            pass
        else:
            if 0 < entrada <= opciones:
                return entrada

def juego():

    j = Jugador('Teo')
    m = Modo(num_preguntas=NUM_PREGUNTAS)

    mi_partida = Partida(j,m)

    mi_partida.iniciar()
    mi_partida.barajar()

    preguntas = mi_partida.preguntas
    cnt_pregunta = 1

    for preg in preguntas:
        cnt_respuesta = 1
        print(f'{cnt_pregunta}/{len(preguntas)}- {preg.cuerpo}')
        cnt_pregunta += 1
        for resp in preg.respuestas:
            print(f'{cnt_respuesta: }: {resp.cuerpo}')
            cnt_respuesta += 1
        entrada = get_entrada(len(preg.respuestas))
        
        if mi_partida.comprobar_resp(preg, preg.respuestas[entrada-1].id):
            j.resultado += 1
            print('**** Respuesta correcta.****\n')
        else:
            print('****Respuesta incorrecta.****')
            print(f'La opción correcta es: {preg.get_resp_correcta()}\n')

    print(f' Jugador: {j.nombre}\n Modo: {m.nombre}\n Marcador: {j.resultado}\n')

def presentacion():
    print('*' * 80)
    print('Juego de Trivial de preguntas con múltiples respuestas ')
    print('*' * 80)
    print('\n\n')

def main():
    borrar_pantalla()
    presentacion()
    juego()


main()

# REF: https://python.plainenglish.io/creating-a-python-powered-quiz-f52f846517e3