import random

# Definizione della tabella di lettere, quantità e punti
lettere_tabella = {
    'a': {'quantità': 14, 'punti': 1},
    'b': {'quantità': 3, 'punti': 5},
    'c': {'quantità': 6, 'punti': 2},
    'd': {'quantità': 3, 'punti': 5},
    'e': {'quantità': 11, 'punti': 1},
    'f': {'quantità': 3, 'punti': 5},
    'g': {'quantità': 2, 'punti': 8},
    'h': {'quantità': 2, 'punti': 8},
    'i': {'quantità': 12, 'punti': 1},
    'l': {'quantità': 5, 'punti': 3},
    'm': {'quantità': 5, 'punti': 3},
    'n': {'quantità': 5, 'punti': 3},
    'o': {'quantità': 15, 'punti': 1},
    'p': {'quantità': 3, 'punti': 5},
    'q': {'quantità': 1, 'punti': 10},
    'r': {'quantità': 6, 'punti': 2},
    's': {'quantità': 6, 'punti': 2},
    't': {'quantità': 6, 'punti': 2},
    'u': {'quantità': 5, 'punti': 3},
    'v': {'quantità': 3, 'punti': 5},
    'z': {'quantità': 2, 'punti': 8}
}

# Caricamento delle parole dal file dizionario
def carica_dizionario():
    with open('parole.txt', 'r', encoding='utf-8') as file:
        return set(parola.strip().lower() for parola in file)

# Estrazione casuale delle lettere per l'utente
def estrai_lettere():
    lettere = []
    for lettera, info in lettere_tabella.items():
        for _ in range(info['quantità']):
            lettere.append(lettera)
    random.shuffle(lettere)
    return lettere[:8]

# Calcolo del punteggio di una parola
def calcola_punteggio(parola):
    punteggio = 0
    for lettera in parola:
        punteggio += lettere_tabella[lettera]['punti']
    return punteggio

# Verifica se la parola è valida e se è presente nel dizionario
def verifica_parola(parola, dizionario):
    #lettere_disponibili = lettere_disponibili.copy()
    
    for lettera in parola:
        if lettera not in lettere_disponibili:
            print("La parola contiene lettere non disponibili.")
            return False
        lettere_disponibili.remove(lettera)
    if parola not in dizionario:
        print("La parola non è presente nel dizionario.")
        return False
    return True

# Funzione principale del gioco
def gioca():
    global lettere_disponibili
    dizionario = carica_dizionario()
    punteggio_tot = 0

    lettere_disponibili = estrai_lettere()
    print("Le lettere che puoi usare sono:", ", ".join(lettere_disponibili))

    while True:
        if(len(lettere_disponibili) < 8):
            lettere_disponibili = estrai_lettere()
            print("Le lettere che puoi usare sono:", ", ".join(lettere_disponibili))
        
        parola = input("Inserisci una parola (o 'fine' per terminare): ")
        parola = parola.lower()
        if parola == 'fine':
            print("Grazie per aver giocato! Il tuo punteggio è ", punteggio_tot)
            break

        if verifica_parola(parola, dizionario):
            punteggio_ora = calcola_punteggio(parola)
            punteggio_tot += punteggio_ora
            print("Punteggio ottenuto:", punteggio_ora) 
            print("Punteggio totale:", punteggio_tot)
            
# Esegui il gioco
gioca()
