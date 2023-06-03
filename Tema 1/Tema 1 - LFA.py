def verifica_cuvinte(gramatica, cuvinte):

    # Verifica daca fiecare cuvant din lista de cuvinte apartine limbajului generat de gramatica
    for cuvant in cuvinte:
        if verifica_cuvant(gramatica, 'S', cuvant):
            print(f"Cuvantul '{cuvant}' apartine limbajului generat de gramatica")
        else:
            print(f"Cuvantul '{cuvant}' NU apartine limbajului generat de gramatica")

def verifica_cuvant(gramatica, simbol_start, cuvant):

    # Verificam daca am ajuns la finalul cuvantului si daca simbolul de start poate sa produca cuvantul vid.
    if not cuvant and 'l' in gramatica[simbol_start]:
        return True

    # Pentru fiecare regula ce poate fi aplicata simbolului de start, incercam sa derivam restul cuvantului.
    for regula in gramatica[simbol_start]:
        # Daca simbolul din regula este o litera mica și cuvantul mai are cel puțin o litera si incepe cu litera respectiva:
        if regula[0].islower() and cuvant and cuvant[0] == regula[0]:
            # Incercam să derivam restul cuvântului pornind de la noul simbol de start.
            if verifica_cuvant(gramatica, regula[1], cuvant[1:]):
                return True

        # Daca simbolul din regula este o litera mare, recursiv apelăm aceeași funcție pentru noul simbol de start si restul cuvantului
        elif regula[0].isupper():
            if verifica_cuvant(gramatica, regula[0], regula[1] + cuvant):
                return True

    # Daca nu am reusit sa derivam cuvantul pornind de la simbolul de start dat, acesta nu apartine limbajului.
    return False


gramatica = {
    'S': [('a', 'A'), ('d', 'E')],
    'A': [('a', 'B'), ('a', 'S')],
    'B': [('b', 'C')],
    'C': [('b', 'D'), ('b', 'B')],
    'D': [('c', 'D'), 'l'],
    'E': ['l']
}

cuvinte = ['aabbdcc', 'abbc', 'abb', 'aad', 'dbc','aaaad']

verifica_cuvinte(gramatica, cuvinte)
