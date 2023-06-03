import random

# Funcția pentru afișarea unui dicționar
def afisare(dictionar):
    for linie in dictionar:
        print(linie, dictionar[linie])
    print()

# Funcția pentru afișarea unei partitii
def afisarePartitie(partitii):
    for partitie in partitii:
        print(partitii.index(partitie))
        for stare in partitie:
            print(stare, partitie[stare])
    print()

# Funcție pentru a verifica dacă două stări sunt aproape egale
def stariAproapeEgale(st1, st2):
    ok = 1
    for litera in alfabet:
        if st1[litera][1] != st2[litera][1]:
            ok = 0
    return ok

# Funcție pentru partitionarea unei liste de partitii
def partitionare(listaPartitii):
    partitieNoua = []
    for partitie in listaPartitii:
        for stare in partitie:
            if len(partitieNoua) == 0 or len(partitie) == 1:  # dacă partitia e goala sau are o sg stare
                partitieNoua.append({stare: partitie[stare]})
            else:
                for x in partitieNoua:
                    if stariAproapeEgale(partitie[stare], x[random.choice(list(x.keys()))]):
                        # Verifica daca starea curenta și o stare aleatoare dintr-o partitie existenta sunt aproape egale
                        x[stare] = partitie[stare]
                        break
                else:
                    partitieNoua.append({stare: partitie[stare]})  # Daca nu s-a gasit partitie, adaugam un dicționar cu cheia stare și valoarea corespunzătoare
    return partitieNoua

# Funcyie pentru reconstruirea partitiilor
def reconstruct(partitii):
    for partitie in partitii:
        for stare in partitie:
            for litera in partitie[stare]:
                for partitie2 in partitii:
                    if partitie[stare][litera][0] in partitie2:
                        partitie[stare][litera][1] = partitii.index(partitie2)

# Citirea datelor de intrare din fisierul "minimalDFA.in"
with open("minimalDFA.in") as f:
    alfabet = f.readline().strip().split()
    finale = f.readline().strip().split()
    tranzitii = f.readline().strip().split()
    dictionar_tranzitii = {}
    for stare in tranzitii:
        dictionar_tranzitii[stare] = {}
    for linie in f:
        tranz = linie.strip().split()
        dictionar_tranzitii[tranz[0]][tranz[1]] = [tranz[2], None]

partitii = []
A = {}
B = {}
# Partitionarea inițială a stărilor în A și B, pe baza stărilor finale
for stare in dictionar_tranzitii:
    if stare in finale:
        B[stare] = dictionar_tranzitii[stare]
    else:
        A[stare] = dictionar_tranzitii[stare]
partitii.append(A)
partitii.append(B)
reconstruct(partitii)

partitieaux = partitionare(partitii)
reconstruct(partitieaux)

# Aplicarea algoritmului de minimizare pana când partitiile se stabilizează
while partitieaux != partitii:
    partitii = partitionare(partitii)
    reconstruct(partitii)

    partitieaux = partitionare(partitieaux)
    reconstruct(partitieaux)

print("Partitii finale dupa minimizare:")
afisarePartitie(partitii)
