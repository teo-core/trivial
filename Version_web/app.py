from settings import TEMPLATES,BD,STATIC_FILES
from bottle import run, route, jinja2_view, TEMPLATE_PATH, request, redirect, static_file
from sql import Sql
from partida import Partida
from jugador import Jugador
from modo import Modo
from settings import NUM_PREGUNTAS

bdatos = Sql(BD)
TEMPLATE_PATH.append(TEMPLATES)

def comprueba_resp(id_pregunta, id_respuesta):
    consulta = f"""SELECT p.id as id_pregunta, r.id as id_respuesta, p.cuerpo as pregunta, r.cuerpo as respuesta from preguntas p join respuestas r on p.id = r.id_pregunta where p.id= {id_pregunta} and r.correcta = 1"""
    resultado = bdatos.select(consulta)[0]
    correcto = int(resultado[1]) == int(id_respuesta)

    return [correcto, [resultado[2], resultado[3]]]


@route('/static/<filename:path>')
def server_static(filename):
    archivo = static_file(filename, root=STATIC_FILES)
    return archivo

@route('/')
@jinja2_view('home.html')
def lista():
    return {}
       
@route('/nueva', method='POST')
@jinja2_view('formulario.html')
def iniciar_partida():
    nombre_jugador = request.POST['jugador']
    j = Jugador(nombre_jugador)
    m = Modo(num_preguntas=NUM_PREGUNTAS)

    mi_partida = Partida(j,m)

    mi_partida.iniciar()
    mi_partida.barajar()


    return {'jugador': nombre_jugador,'preguntas': mi_partida.preguntas}


@route('/save', method='POST')
@jinja2_view('resultado.html')
def save():
    marcador = 0
    salida = []
    datos = request.POST.dict
    jugador_actual = datos['jugador'][0]
    for k,v in datos.items():
        if 'pregunta' in k:
            validacion = comprueba_resp(v[0],v[1])
            if validacion[0]:
                marcador += 1
            salida.append(validacion)
            
    return {'jugador':jugador_actual, 'resultados':salida, 'marcador': marcador}






run(host='localhost', port=8080,debug=True,reloader=True)

