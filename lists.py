# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    length = len(list_to_remove_elements)

    if length >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif length < 6 and length <= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif length < 5 and length > 0:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif length == 0:
        return list_to_remove_elements
list_to_remove_elements=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list_to_remove_elements))




def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return lista


def is_empty(list_to_check):
    if len(list_to_check)>0:
        return 'La lista no esta vacia'
    else:
        return 'La lista esta vacia'

print(is_empty([]))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else: 
            return False
    else: False    

print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))

def list_of_lists(list_of_lists_to_modify):
    lista1 = lista[0]
    lista2 = lista[1]
    lista3 = lista[2]
    del lista1[2:]
    del lista2[4:]
    del lista2[0]
    del lista3[:-2]
    return lista

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
