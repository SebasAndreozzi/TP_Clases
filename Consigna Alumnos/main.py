"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
from class_video import *
from data import *
from video_generales import *
from Input import get_string

message_a = "A. NORMALIZAR OBJETOS"
message_b = "B. MOSTRAR TEMAS"
message_c = "C. ORDENAR TEMAS"
message_d = "D. PROMEDIO DE VISTAS"
message_e = "E. MAXIMA REPRODUCCION"
message_f = "F. BUSQUEDA POR CODIGO"
message_g = "G. LISTAR POR COLABORADOR"
message_h = "H. LISTAR POR MESS"
message_i = "I. SALIR"

message_abc = f"{message_a}\n{message_b}\n{message_c}\n"
message_def = f"{message_d}\n{message_e}\n{message_f}\n"
message_ghi = f"{message_g}\n{message_h}\n{message_i}\n"

message_input_final = f"{message_abc}{message_def}{message_ghi}"

message_input_error = "Debe ingresar un solo caracter: "

message_input_miss = "No ingresó una opción valida. Intente de nuevo."

message_input_retry = "Agotó el número de reintentos. Vuelva a iniciar."

message_input_no_a = "Primero debe normalizar orbjetos (opción A)"

entry_flag = False

while True:

    entry = get_string(message_input_final, message_input_error, 1, 3)

    match entry:

        case "A":

            for i in range(len(lista_videos)):
                Video.dividir_titulo(lista_videos[i])
                Video.obtener_codigo_url(lista_videos[i])
                Video.formatear_fecha(lista_videos[i])

            entry_flag = True   
        case "B":
            if entry_flag:
                for i in range(len(lista_videos)):
                    Video.mostrar_tema(lista_videos[i])
            else:
                print(message_input_no_a)
                pass
        case "C":
            if entry_flag:
                min_to_max(lista_videos)
                for i in range(len(lista_videos)):
                    Video.mostrar_tema(lista_videos[i])
            else:
                print(message_input_no_a)
                pass

        case "D":
            if entry_flag:
                
                print(f"El promedio de vistas es: {average_views(lista_videos)}")
            else:
                print(message_input_no_a)
                pass
        case "E":
            if entry_flag:
                max_list = max_views_list(lista_videos)
                for i in range(len(max_list)):
                    Video.mostrar_tema(lista_videos[max_list[i]])
            else:
                print(message_input_no_a)
                pass
        case "F":
            if entry_flag:
                pass
            else:
                print(message_input_no_a)
                pass
        case "G":
            if entry_flag:
                pass
            else:
                print(message_input_no_a)
                pass
        case "H":
            if entry_flag:
                pass
            else:
                print(message_input_no_a)
                pass
        case "I":
            break
        case _:
            print(message_input_miss)
            pass
