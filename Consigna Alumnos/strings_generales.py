###COMPARA 2 STRINGS. DEVUELVE TRUE SI SON IGUALES Y FALSE SI SON DISTINTOS
def compare_string(first_string:str, second_string:str) -> bool:
    result = False

    for j in range((len(first_string)-len(second_string))+1):
        same_string = True

        for x in range(len(second_string)):
            if first_string[j+x]!=second_string[x]:
                same_string = False
                break
        
        if same_string:
            result = True
    
    return result