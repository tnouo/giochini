def stampa(S):
    for riga in S:
        print(riga)
    return

def generaTabella():
    S = []
    for i in range(8):
        riga = []
        for j in range(8):
            riga.append("[ ]")
        S.append(riga)
    S[3][3] = "[B]"
    S[3][4] = "[N]"
    S[4][3] = "[N]"
    S[4][4] = "[B]"
    return S

def cambioTurno(turno):
    if turno == "[N]":
        turno = "[B]"
    else:
        turno = "[N]"
    return turno

def vincitore(S):
    contaNeri = 0
    contaBianchi = 0
    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] == "[N]":
                contaNeri += 1
            elif S[i][j] == "[B]":
                contaBianchi += 1
    v = "PAREGGIO"
    if contaNeri > contaBianchi:
        v = "Nero"
    elif contaBianchi > contaNeri:
        v = "Bianco"
    return v

def conta_catture_verticale(S, c, i, j):
    # Il metodo restituisce il numero di catture fatte nelle due direzioni verticali
    cattura = False

    # Cerchiamo nella parte superiore
    i1 = i - 1
    cont_s = 0

    # Parte superiore
    if i1 >= 0 and S[i1][j] != c and S[i1][j] != '[ ]':
        # Nella cattura non ci devono essere caselle vuote
        while i1 >= 0 and not cattura and S[i1][j] != '[ ]':
            # Chiusura cattura (cerchiamo l'altra pedina di colore c)
            if S[i1][j] == c:
                cattura = True
            else:
                cont_s += 1
            i1 -= 1
        if cattura == False:
            cont_s = 0

    # Parte inferiore
    cattura = False
    cont_i = 0
    i1 = i + 1
    if i1 < len(S) and S[i1][j] != c and S[i1][j] != "[ ]":
        while i1 < len(S) and not cattura and S[i1][j] != "[ ]":
            if S[i1][j] == c:
                cattura = True
            else:
                cont_i += 1
            i1 += 1
        if cattura == False:
            cont_i = 0

    return cont_s + cont_i

def conta_catture_orizzontale(S, c, i, j):
    cattura = False

    j1 = j - 1
    cont_sx = 0

    if j1 >= 0 and S[i][j1] != c and S[i][j] != "[ ]":
        while j1 >= 0 and not cattura and S[i][j1] != "[ ]":
            if S[i][j1] == c:
                cattura = True
            else:
                cont_sx += 1
            j1 -= 1
        if cattura == False:
            cont_sx = 0

    cattura = False
    j1 = j + 1
    cont_dx = 0
    if j1 < len(S[i]) and S[i][j1] != c and S[i][j1] != "[ ]":
        while j1 < len(S[i]) and not cattura and S[i][j1] != "[ ]":
            if S[i][j1] == c:
                cattura = True
            else:
                cont_dx += 1
            j1 += 1
        if cattura == False:
            cont_dx = 0
    return cont_dx + cont_sx

def conta_diagonale_principale(S, c, i, j):
    # parte superiore
    cattura = False

    i1 = i - 1
    j1 = j - 1

    cont_s = 0

    if i1 >= 0 and j1 >= 0 and S[i1][j1] != c and S[i1][j1] != '[ ]':
        # Nella cattura non ci devono essere caselle vuote
        while i1 >= 0 and j1 >= 0 and not cattura and S[i1][j1] != '[ ]':
            # Chiusura cattura (cerchiamo l'altra pedina di colore c)
            if S[i1][j1] == c:
                cattura = True
            else:
                cont_s += 1
            i1 -= 1
            j1 -= 1
        if cattura == False:
            cont_s = 0

    # parte inferiore
    cattura = False

    i1 = i + 1
    j1 = j + 1

    cont_i = 0

    if i1 < len(S) and j1 < len(S[i1]) and S[i1][j1] != c and S[i1][j1] != "[ ]":
        while i1 < len(S) and j1 < len(S[i1]) and not cattura and S[i1][j1] != "[ ]":
            if S[i1][j1] == c:
                cattura = True
            else:
                cont_i += 1
            i1 += 1
            j1 += 1
        if cattura == False:
            cont_i = 0
    return cont_i + cont_s

def conta_diagonale_secondaria(S, c, i, j):
    # parte superiore
    cattura = False

    i1 = i - 1
    j1 = j + 1

    cont_s = 0

    if i1 >= 0 and j1 < len(S[i1]) and S[i1][j1] != c and S[i1][j1] != "[ ]":
        while i1 >= 0 and j1 < len(S[i1]) and not cattura and S[i1][j1] != "[ ]":
            if S[i1][j1] == c:
                cattura = True
            else:
                cont_s += 1
            i1 -= 1
            j1 += 1
        if cattura == False:
            cont_s = 0

    # parte inferiore
    cattura = False

    i1 = i + 1
    j1 = j - 1

    cont_i = 0

    if i1 < len(S) and j1 >= 0 and S[i1][j1] != c and S[i1][j1] != "[ ]":
        while i1 < len(S) and j1 >= 0 and not cattura and S[i1][j1] != "[ ]":
            if S[i1][j1] == c:
                cattura = True
            else:
                cont_i += 1
            i1 += 1
            j1 -= 1
        if cattura == False:
            cont_i = 0
    return cont_i + cont_s

def contaCatture(S, i, j, c):
    conta_catture = 0
    if S[i][j] == '[ ]':
        conta_catture = conta_catture_verticale(S, c, i, j) + conta_catture_orizzontale(S, c, i, j) + conta_diagonale_principale(S, c, i, j) + conta_diagonale_secondaria(S, c, i, j)
    return conta_catture

def esisteMossaValida(S):
    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] == "[ ]" and (contaCatture(S, i, j, "[N]") > 0 or contaCatture(S, i, j, "[B]") > 0):
                return True
    return False

def mossa(S, c, i, j):
    mossa_valida = False
    numCatture = contaCatture(S, i, j, c)
    if numCatture > 0:
        mossa_valida = True

        S[i][j] = c

        # cattura verticale
        # parte superiore
        cattura = False

        i1 = i - 1

        if i1 >= 0 and S[i1][j] != c and S[i1][j] != '[ ]':
            # Nella cattura non ci devono essere caselle vuote
            while i1 >= 0 and not cattura and S[i1][j] != '[ ]':
                # Chiusura cattura (cerchiamo l'altra pedina di colore c)
                if S[i1][j] == c:
                    cattura = True
                else:
                    S[i1][j] = c
                i1 -= 1

        # parte inferiore
        cattura = False

        i1 = i + 1

        if i1 < len(S) and S[i1][j] != c and S[i1][j] != "[ ]":
            while i1 < len(S) and not cattura and S[i1][j] != "[ ]":
                if S[i1][j] == c:
                    cattura = True
                else:
                    S[i1][j] = c
                i1 += 1

        # cattura orizzontale
        # parte destra
        cattura = False

        j1 = j + 1

        if j1 < len(S[i]) and S[i][j1] != c and S[i][j1] != "[ ]":
            while j1 < len(S[i]) and not cattura and S[i][j1] != "[ ]":
                if S[i][j1] == c:
                    cattura = True
                else:
                    S[i][j1] = c
                j1 += 1
        # parte sinistra
        cattura = False

        j1 = j - 1

        if j1 >= 0 and S[i][j1] != c and S[i][j1] != "[ ]":
            while j1 >= 0 and not cattura and S[i][j1] != "[ ]":
                if S[i][j1] == c:
                    cattura = True
                else:
                    S[i][j1] = c
                j1 -= 1

        # cattura diagonale principale
        # parte superiore
        cattura = False

        i1 = i - 1
        j1 = j - 1

        if i1 >= 0 and j1 >= 0 and S[i1][j1] != c and S[i1][j1] != "[ ]":
            while i1 >= 0 and j1 >= 0 and not cattura and S[i1][j1] != "[ ]":
                if S[i1][j1] == c:
                    cattura = True
                else:
                    S[i1][j1] = c
                i1 -= 1
                j1 -= 1
        # parte inferiore
        cattura = False

        i1 = i + 1
        j1 = j + 1

        if i1 < len(S) and j1 < len(S[i1]) and S[i1][j1] != c and S[i1][j1] != "[ ]":
            while i1 < len(S) and j1 < len(S[i1]) and not cattura and S[i1][j1] != "[ ]":
                if S[i1][j1] == c:
                    cattura = True
                else:
                    S[i1][j1] = c
                i1 += 1
                j1 += 1

        #cattura diagonale secondaria
        # parte superiore
        cattura = False

        i1 = i - 1
        j1 = j + 1

        if i1 >= 0 and j1 < len(S[i1]) and S[i1][j1] != c and S[i1][j1] != "[ ]":
            while i1 >= 0 and j1 < len(S[i1]) and not cattura and S[i1][j1] != "[ ]":
                if S[i1][j1] == c:
                    cattura = True
                else:
                    S[i1][j1] = c
                i1 -= 1
                j1 += 1

        # parte inferiore
        cattura = False

        i1 = i + 1
        j1 = j - 1

        if i1 < len(S) and j1 >= 0 and S[i1][j1] != c and S[i1][j1] != "[ ]":
            while i1 < len(S) and j1 >= 0 and S[i1][j1] != "[ ]":
                if S[i1][j1] == c:
                    cattura = True
                else:
                    S[i1][j1] = c
                i1 += 1
                j1 -= 1

    return mossa_valida

def fine(S):
    partitaFinita = False
    if not esisteMossaValida(S):
        print("Partita finita, il vincitore è "+vincitore(S))
        partitaFinita = True
    return partitaFinita

def effettuaMossa(S, turno):
    # controllo delle coordinate
    casellaOccupata = True
    valida = False
    while casellaOccupata:
        print("Inserire le coordinate i e j: ")
        # controllo dell'indice i
        valid = False
        while not valid:
            i = input("i: ")
            while not i.isdigit():
                i = input("i: ")
            i = int(i)
            if i >= 0 and i < len(S):
                valid = True
        # controllo dell'indice j
        valid = False
        while not valid:
            j = input("j: ")
            while not j.isdigit():
                j = input("j: ")
            j = int(j)
            if j >= 0 and j < len(S):
                valid = True
        if S[i][j] == "[ ]":
            casellaOccupata = False
        else:
            print("Casella già occupata")
        if mossa(S, turno, i, j):
            valida = True
        else:
            print("Mossa non valida")
            casellaOccupata = True  # riutilizzo questa variabile così che se la mossa non è valida richiede all'utente delle nuove coordinate

def Othello():
    S = generaTabella()
    turno = input("Chi inizia? (B/N)")
    turno = turno.upper()
    while turno != "B" and turno != "N":
        turno = input("Chi inizia? (B/N)")
        turno = turno.upper()
    turno = "["+turno+"]"
    stampa(S)
    while not fine(S):
        if turno == "[B]":
            print("è il turno dei Bianchi")
        else:
            print("è il turno dei Neri")
        effettuaMossa(S, turno)
        stampa(S)
        turno = cambioTurno(turno)
    print("Gioco finito\nIl vincitore è "+vincitore(S))
    return

def main_Othello():
    print("REGOLE DEL GIOCO\nogni giocatore deve posizionare la sua pedina in modo tale da catturare almeno una pedina avversarisa,\nuna mossa non è valida se non vengono effettuate catture\nse non è più possibile effettuare mosse il gioco finisce e il vincitore è colui che ha più pedine in campo\n\nBuon divertimento!\n")
    input("Premere INVIO per iniziare")
    rigioca = "S"
    while rigioca == "S":
        Othello()
        rigioca = input("Vuoi rigiocare? (S/N)")
        rigioca.upper()
        while rigioca != "S" and rigioca != "N":
            rigioca = input("Vuoi rigiocare? (S/N)")
            rigioca.upper()
    return

main_Othello()
