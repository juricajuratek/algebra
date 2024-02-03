"""ZADATAK 1: Ukloniti duplikate (u listi) u finkciji process_list koristeci 2 preddfinirane funkcije"""
"""Napomena predefinirane algebrine funkcije mozda ne izgledaju identicno"""

def find_duplicates(lista):
    """Algebrina funkcija koja trazi duplikate"""
    seen = set()
    duplicates = set()
    for item in lista:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return duplicates


def remove_duplicates(lista):
    """Algebrina funkcija za uklanjanje duplikata"""
    return list(set(lista))


"""Ova funkcija nam je u ispitu prazna i mi moramo implementirati gornje dvije algebrine funkcije"""
def process_list(lista):
    duplicates = find_duplicates(lista)
    print(f"Duplicates found: {duplicates}")
    new_list = remove_duplicates(lista)
    return new_list



lista = (1, 2, 3, 4, 4, 3, 2, 1, 4, 5, 6, 4, 6, 3, 7, 1, 0, 9, 8)

results = process_list(lista)
print(f"List without duplicates: {results}")