def posizionaDifesaTest(D):
    p = [[4], [0]]

    i1 = [[3], [0]]
    i2 = [[3], [0]]

    v1 = [[2], [0]]
    v2 = [[2], [0]]
    v3 = [[2], [0]]

    s1 = [[1], [0]]
    s2 = [[1], [0]]
    s3 = [[1], [0]]
    s4 = [[1], [0]]

    D[0][0] = p
    D[0][1] = p
    D[0][2] = p
    D[0][3] = p

    D[1][5] = i1
    D[2][5] = i1
    D[3][5] = i1

    D[4][7] = i2
    D[4][8] = i2
    D[4][9] = i2

    D[2][1] = v1
    D[2][2] = v1

    D[8][3] = v2
    D[8][4] = v2

    D[6][7] = v3
    D[7][7] = v3

    D[0][8] = s1

    D[4][3] = s2

    D[6][1] = s3

    D[9][9] = s4

def stampa(M):
    for riga in M:
        print(riga)
def generaAttacco():
    A = []
    for i in range(10):
        riga = []
        for j in range(10):
            riga.append(" ")
        A.append(riga)
    return A

def posiziona(D):
    p = [[4],[0]]

    i1 = [[3],[0]]
    i2 = [[3],[0]]

    v1 = [[2],[0]]
    v2 = [[2],[0]]
    v3 = [[2],[0]]

    s1 = [[1],[0]]
    s2 = [[1],[0]]
    s3 = [[1],[0]]
    s4 = [[1],[0]]

    # posiziona portaerei
    print("Inserire le coordinate della portaerei")
    for n in range(4):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = p
    # posiziona incrociatore 1
    print("Inserire le coordinate dell'incrociatore 1")
    for n in range(3):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = i1
    #posiziona incrociatore 2
    print("Inserire le coordinate dell'incrociatore 2")
    for n in range(3):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = i2
    #posiziona vedetta 1
    print("Inserire le coordinate della vedetta 1")
    for n in range(2):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = v1
    # posiziona vedetta 2
    print("Inserire le coordinate della vedetta 2")
    for n in range(2):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = v2
    # posiziona vedetta 3
    print("Inserire le coordinate della vedetta 3")
    for n in range(2):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = v3
    # posiziona sottomarino 1
    print("Inserire le coordinate del sottomarino 1")
    for n in range(1):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = s1
    # posiziona sottomarino 2
    print("Inserire le coordinate del sottomarino 2")
    for n in range(1):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = s2
    # posiziona sottomarino 3
    print("Inserire le coordinate del sottomarino 3")
    for n in range(1):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = s3
    # posiziona sottomarino 4
    print("Inserire le coordinate del sottomarino 4")
    for n in range(1):
        x = int(input("x: "))
        y = int(input("y: "))
        while D[x][y] != " ":
            print("casella occupata")
            x = int(input("x: "))
            y = int(input("y: "))
        D[x][y] = s4
    return

def generaDifesa():
    D = []
    for i in range(10):
        riga = []
        for j in range(10):
            riga.append(" ")
        D.append(riga)
    posiziona(D)
    #posizionaDifesaTest(D)
    return D

def generaInterfacciaDifesa(D):
    interfacciaD = generaAttacco()
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] != " ":
                if D[i][j][0][0] == 1:
                    interfacciaD[i][j] = "S"
                elif D[i][j][0][0] == 2:
                    interfacciaD[i][j] = "V"
                elif D[i][j][0][0] == 3:
                    interfacciaD[i][j] = "I"
                elif D[i][j][0][0] == 4:
                    interfacciaD[i][j] = "P"
            else:
                interfacciaD[i][j] = " "
    return interfacciaD

def haPerso(D):
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] != " " and D[i][j][0][0] > 0:
                return False
    return True

def fine(D1, D2):
    if haPerso(D1) or haPerso(D2):
        return True
    else:
        return False

def vincitore(D1):
    if haPerso(D1):
        return "G2"
    else:
        return "G1"

def attacco(A, D, Dui):
    print("ATTACCO")
    stampa(A)
    print("Inserire le coordinate da attaccare")
    x = int(input("x: "))
    y = int(input("y: "))
    while A[x][y] != " ":
        print("non puoi colpire più volte nella stessa casella")
        x = int(input("x: "))
        y = int(input("y: "))
    if D[x][y] == " ":
        A[x][y] = "X"
        stampa(A)
        input("Acqua (premi INVIO per continuare)")
        return False
    else:
        D[x][y][0][0] -= 1
        A[x][y] = D[x][y][1]
        Dui[x][y] = "X"
        if D[x][y][0][0] > 0:
            stampa(A)
            input("Colpito (premi INVIO per continuare)")
        else:
            D[x][y][1][0] += 1
            stampa(A)
            input("Affondato (premi INVIO per continuare)")
        return True

def BattagliaNavale():
    A1 = generaAttacco()
    A2 = generaAttacco()
    D1 = generaDifesa()
    D1ui = generaInterfacciaDifesa(D1)
    D2 = generaDifesa()
    D2ui = generaInterfacciaDifesa(D2)
    turno = int(input("Chi inizia? (1/2)"))
    for i in range(300):
        print()
    turnoCambiato = False
    while not fine(D1, D2):
        if turnoCambiato == True:
            turnoCambiato = False
            for i in range(300):
                print()
        if turno%2==0:
            input("è il turno di G2 (premi INVIO)\n")
            for i in range(300):
                print()
            print("NAVI")
            stampa(D2ui)
            print()
            if not attacco(A2, D1, D1ui):
                turno+=1
                turnoCambiato = True
        else:
            input("è il turno di G1 (premi INVIO)\n")
            for i in range(300):
                print()
            print("NAVI")
            stampa(D1ui)
            print()
            if not attacco(A1, D2, D2ui):
                turno+=1
                turnoCambiato = True
    print("Fine, il vincitore è "+vincitore(D1))
    return


BattagliaNavale()