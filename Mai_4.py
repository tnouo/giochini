from random import randint

def leggiM():
    n = int(input("Inserire la dimensione della tabella"))
    M = []
    for i in range(n):
        riga = []
        for j in range(n):
            riga.append(input("Inserire la casella di indice "+i+";"+j))
        M.append(riga)
    return M

def fine(M):
    finito = True
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == "[   ]" and (valido(M, i, j, '[ X ]') or valido(M, i, j, '[ O ]')):
                finito = False
    return finito

def c_v(M, i, j, a):
    valido = True
    conta = 1
    # parte superiore
    adiacente = True
    i1 = i-1
    while i1>=0 and adiacente:
        if M[i1][j] == a:
            conta += 1
        else:
            adiacente = False
        i1 -= 1

    # parte inferiore
    adiacente = True
    i1 = i+1
    while i1<len(M) and adiacente:
        if M[i1][j] == a:
            conta += 1
        else:
            adiacente = False
        i1+=1
    if conta >= 4:
        valido = False
    return valido

def c_o(M, i, j, a):
    valido = True
    conta = 1
    # parte destra
    adiacente = True
    j1 = j+1
    while j1<len(M[i]) and adiacente:
        if M[i][j1] == a:
            conta += 1
        else:
            adiacente = False
        j1 += 1

    # parte sinistra
    adiacente = True
    j1 = j-1
    while j1>=0 and adiacente:
        if M[i][j1] == a:
            conta += 1
        else:
            adiacente = False
        j1 -= 1

    if conta >= 4:
        valido = False
    return valido

def c_dp(M, i, j, a):
    valido = True
    conta = 1
    # parte superiore
    i1 = i-1
    j1 = j-1
    adiacente = True
    while i1>=0 and j1>=0 and adiacente:
        if M[i1][j1] == a:
            conta *= 1
        else:
            adiacente = False
        i1-=1
        j1-=1

    # parte inferiore
    i1 = i+1
    j1 = j+1
    adiacente = True
    while i1<len(M) and j1<len(M[i1]):
        if M[i1][j1] == a:
            conta += 1
        else:
            adiacente = False
        i1+=1
        j1+=1

    if conta>=4:
        valido = False
    return valido

def c_ds(M, i, j, a):
    conta = 1
    valido = True
    # parte superiore
    i1 = i-1
    j1 = j+1
    adiacente = True
    while i1>=0 and j1<len(M[i1]) and adiacente:
        if M[i1][j1] == a:
            conta += 1
        else:
            adiacente = False
        i1-=1
        j1+=1

    # parte inferiore
    i1 = i+1
    j1 = j-1
    adiacente = True
    while i1<len(M) and j1>=0 and adiacente:
        if M[i1][j1] == a:
            conta += 1
        else:
            adiacente = False
        i1+=1
        j1-=1

    if conta>=4:
        valido = False
    return valido

def valido(M, i, j, a):
    if M[i][j] != '[   ]':
        return False
    return c_v(M, i, j, a) and c_o(M, i, j, a) and c_dp(M, i, j, a) and c_ds(M, i, j, a)

def inserimento(M):
    casellaOccupata = True
    while casellaOccupata:
        print("Inserire le coordinate i e j: ")
        # controllo dell'indice i
        valid = False
        while not valid:
            i = input("i: ")
            while not i.isdigit():
                i = input("i: ")
            i = int(i)
            if i>=0 and i<len(M):
                valid = True
        # controllo dell'indice j
        valid = False
        while not valid:
            j = input("j: ")
            while not j.isdigit():
                j = input("j: ")
            j = int(j)
            if j>=0 and j<len(M):
                valid = True
        # controllo della casella (se è vuota allora prosegui con l'inserimento)
        if M[i][j] == '[   ]':
            casellaOccupata = False
        else:
            print("Posizione non valida, casella già occupata")

    a = input("Inserire il valore X o O da inserire nella casella: ")
    a = a.upper()
    while a != 'X' and a != 'O':
        a = input("Inserire il valore X o O da inserire nella casella: ")
        a = a.upper()
    a = '[ ' + a + ' ]'
    ok = False
    if valido(M, i, j, a):
        M[i][j] = a
        ok = True
    else:
        print("Posizione non valida")
    return ok

def generaCasuali(M):
    n = len(M)
    numX = randint(0, 3)
    numO = randint(0, 3)

    # genera random X
    for x in range(numX):
        a = randint(0, n-1)
        b = randint(0, n-1)
        while M[a][b] != '[   ]':
            a = randint(0, n - 1)
            b = randint(0, n - 1)
        M[a][b] = '[ X ]'
    # genera random O
    for o in range(numO):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        while M[a][b] != '[   ]':
            a = randint(0, n - 1)
            b = randint(0, n - 1)
        M[a][b] = '[ O ]'
    return

def generaTabella():
    M = []
    corretto = False
    while not corretto:
        n = input("Inserire la dimensione (>=4) della tabella di gioco: ")
        while not n.isdigit():
            n = input("Inserire la dimensione (>=4) della tabella di gioco: ")
        n = int(n)
        if n<4:
            print("Dimensione non valida (<4)")
        else:
            corretto = True
    for i in range(n):
        riga = []
        for j in range(n):
            riga.append('[   ]')
        M.append(riga)
    generaCasuali(M)
    return M

def stampa(M):
    for riga in M:
        print(riga)
    return

def Mai_4():
    M = generaTabella()
    stampa(M)
    finito = False
    while not finito:
        while not finito and inserimento(M):
            stampa(M)
            if fine(M):
                finito = True
    print("Gioco finito")

def main_Mai_4():
    print("'''MAI 4'''\nby una traccia del corso di Informatica...\n\nREGOLE DEL GIOCO\npuoi posizionare due tipi di pedine: X o O\nogni pedina non può avere più di 3 pedine dello stesso tipo adicenti sulla stessa riga, colonna o diagonale.\n\nBuon divertimento!")
    input("\npremi INVIO per iniziare")
    rigioca = "S"
    while rigioca == "S":
        Mai_4()
        rigioca = input("\nVuoi rigiocare? (S/N): ")
        rigioca.upper()
        while rigioca != "S" and rigioca != "N":
            rigioca = input()
            rigioca.upper()

# main
main_Mai_4()