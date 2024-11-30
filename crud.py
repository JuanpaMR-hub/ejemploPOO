from clases import Musico, Banda
from bd import hacer_consulta



def crear_musico():
    id_musico = input("ID musico: ")
    nombre_musico = input("Nombre musico: ")
    instrumento = input("Que instrumento toca?  ")
    m = Musico(id_musico,nombre_musico,instrumento)
    print(m)
    confirmation = input("Está correcto? (Y/N) ")
    if confirmation.lower() == 'y':
        try:
            m.guardar_musico()
        except Exception as e:
            print("Hubo un error al guardar al musico: ",e)
        else:
            print("Musico guardado correctamente")

def crear_banda():
    id_banda = input("ID banda")
    nombre_banda = input("Nombre de la banda: ")
    b = Banda(id_banda,nombre_banda)
    print(b)
    confirmation = input("Está correcto? (Y/N) ")
    if confirmation.lower() == 'y':
        try:
            b.guardar_banda()
        except Exception as e:
            print(f"Hubo un error al guardar la banda {b.nombre_banda}")
        else:
            print(f"Banda {b.nombre_banda} guardada correctamente")



def mostrar_objetos(tabla):
    query = f"SELECT * FROM {tabla}"
    resultados = hacer_consulta(query,'select')
    for r in resultados:
        print(r)

def listar_objetos(tabla):
    query = f"SELECT * FROM {tabla}"
    try:
        resultados = hacer_consulta(query,'select')
    except Exception as e:
        print(f"Error al traer tabla {tabla}")
    else:
        objeto = tabla.capitalize()
        objetos = {}
        if objeto == 'Musico':
            for r in resultados:
                objetos[r[0]] = Musico(r[0],r[1],r[2],r[3])
        elif objeto == 'Banda':
            for r in resultados:
                objetos[r[0]] = Banda(r[0],r[1])
        return objetos

    



def asociar_banda_musico():
    musicos = listar_objetos('MUSICO')
    bandas = listar_objetos('BANDA')
    print("############## ELECCION DE MUSICO ##############")
    for musico in musicos.values():
        print(f"{musico.id_musico}. {musico.nombre_musico}")
    musico = int(input("Que musico quiere asociar? "))
    print(musicos[musico])
    for banda in bandas.values():
        print(f"{banda.id_banda}. {banda.nombre_banda}")
    banda = int(input(f"A que banda pertenece {musicos[musico].nombre_musico}?: (numero) "))
    musicos[musico].add_banda(bandas[banda])



def eliminar_musico():
    musicos = listar_objetos("MUSICO")
    for musico in musicos.values():
        print(f"{musico.id_musico}. {musico.nombre_musico}")
    musico = int(input("Que musico quiere eliminar? "))

    try:
        musicos[musico].eliminar_musico()
    except Exception as e:
        print(f"Error al eliminar musico {musicos[musico].nombre_musico}")
    else:
        print(f"Musico {musicos[musico].nombre_musico} eliminado correctamente")


# DEMOSTRACION DEL FUNCIONAMIENTO
crear_musico()
crear_banda()
asociar_banda_musico()
mostrar_objetos()
