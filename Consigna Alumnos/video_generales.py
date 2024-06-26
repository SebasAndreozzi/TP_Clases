from datetime import datetime
from class_video import *
from strings_generales import *
###ORDENAR MIN TO MAX
def min_to_max(lista:list):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j].sesion > lista[j+1].sesion:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar

def average_views(list:list) -> float:
    total = 0

    for i in range(len(list)):
        total += list[i].vistas
    
    result = round((total / len(list)), 2)

    return result

def max_views(list:list) -> int:
    max = 0
    first_entry = True

    for i in range(len(list)):
        if first_entry:
            max = list[i].vistas
            first_entry = False
        else:
            if max < list[i].vistas:
                max = list[i].vistas
    
    return max

def max_views_list(list:list) -> list:
    max = max_views(list)
    video_positions = []

    for i in range(len(list)):
        if list[i].vistas == max:
            video_positions.append(i)
    
    return video_positions
        
def filter_code(list:list, code:str) -> list:
    result = []

    for i in range(len(list)):
        url_code = list[i].codigo_url

        if compare_string(url_code, code):
            result.append(list[i])
    
    return result

def filter_colab(list:list, entry:str) -> list:
    entry = entry.upper()
    result = []

    for i in range(len(list)):
        colab = (list[i].colaborador).upper()

        if compare_string(colab, entry):
            result.append(list[i])
    
    return result

def release_month_list(list:list, month:int) -> list:
    result = []

    for i in range(len(list)):
        release_date = list[i].fecha_lanzamiento
        
        if int(release_date.strftime("%m")) == month:
            result.append(list[i])
    
    return result
