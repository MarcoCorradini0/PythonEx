# Es1: Creare una tupla con i giorni della settimana e stampare(1. Lunedì primo elemento, 2. Domenica ultimo elemento, Quanti giorni ci sono)
"""
giorni=("Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica")
print("Primo giorno della settimana:", giorni[0])
print("Ultimo giorno della settimana:", giorni[-1])
print("Numero di giorni nella settimana:", len(giorni))
"""

# Es2: Creare una tupla con nome, cognome ed età. Usa l'unpacking per assegnare ogni valore a una variabile separata e stampale.
"""
persona=("Mario", "Rossi", 30)
nome, cognome, eta = persona
print(nome, "", cognome, "", eta)
"""

# Es3: Creare 3 tuple per rappresentare 3 punti nel piano (x,y). Punto A(0,0) - Punto B(3,4) - Punto C(6,8) Calcolare la distanza del punto B dall'origine (punto A) usando pitagora.
"""
A=(0,0)
B=(3,4)
C=(6,8)
distanza_B_A=((B[0]-A[0])**2+(B[1]-A[1])**2)**0.5
print("Distanza del punto B dall'origine A:", distanza_B_A)
"""
# Es4: Creare una tupla numeri=(5,2,8,2,9,2,1). A conta quante volte appare il 2 - B Trovare l'indice della prima occorrenza di 8.
"""
numeri=(5,2,8,2,9,2,1)
print("Il numero 2 appare", numeri.count(2), "volte.")
print("Il numero 8 appare per la prima volta all'indice:", numeri.index(8))
"""
# Es5: Conversione lista <-> tupla. A Creare una lista di 4 città. B Convertirla in tupla. C Verifica che la tupla non può essere modificata. D Riconvertirla in lista e aggiungere una città.
citta_lista=["Roma", "Milano", "Napoli", "Torino"]
citta_tupla=tuple(citta_lista)
print("Tupla delle città:", citta_tupla)
#citta_tupla[0]="Milano" verifica modificabilità tupla
citta_lista_nuova=list(citta_tupla)
aggiorna="Firenze"
citta_lista_nuova.append(aggiorna)
print(aggiorna, "aggiunta alla lista delle città:", citta_lista_nuova)