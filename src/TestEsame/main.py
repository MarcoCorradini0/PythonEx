# Importazione librerie necessarie
import os
import math
import statistics
from collections import Counter
from functools import reduce
from math import gcd


# =========================
# UTILS
# =========================

# Funzione per pulire la console
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Pausa del programma per leggere il risultato
def pausa():
    input("\nPremi invio per continuare...")


# Input lista di numeri interi
def input_lista_int():
    return list(map(int, input("Inserisci numeri separati da spazio: ").split()))


# Input lista di numeri float
def input_lista_float():
    return list(map(float, input("Inserisci numeri separati da spazio: ").split()))


# =========================
# ORDINAMENTI E LISTE
# =========================

# Ordinamento crescente
def ordinamento_crescente():
    lista = input_lista_int()
    print(sorted(lista))


# Ordinamento decrescente
def ordinamento_decrescente():
    lista = input_lista_int()
    print(sorted(lista, reverse=True))


# Ordinamento alternato max-min-max-min
def ordinamento_misto():
    lista = sorted(input_lista_int())
    risultato = []

    while lista:
        risultato.append(lista.pop())

        if lista:
            risultato.append(lista.pop(0))

    print(risultato)


# Inverte una lista
def inversione_lista():
    lista = input_lista_int()
    print(lista[::-1])


# Conta le occorrenze degli elementi
def conteggio_occorrenze():
    lista = input_lista_int()
    print(dict(Counter(lista)))


# Rimozione duplicati
def rimuovi_duplicati():
    lista = input_lista_int()
    print(list(set(lista)))


# Divisione numeri pari e dispari
def pari_dispari():
    lista = input_lista_int()

    pari = [x for x in lista if x % 2 == 0]
    dispari = [x for x in lista if x % 2 != 0]

    print("Pari:", pari)
    print("Dispari:", dispari)


# Controllo numero primo
def is_primo(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True


# Estrazione numeri primi
def estrazione_primi():
    lista = input_lista_int()
    print([x for x in lista if is_primo(x)])


# Ricerca elemento nella lista
def ricerca_elemento():
    lista = input_lista_int()
    valore = int(input("Elemento da cercare: "))

    indici = [i for i, x in enumerate(lista) if x == valore]

    if indici:
        print("Indici trovati:", indici)
    else:
        print("Elemento non trovato")


# Verifica lista palindroma
def lista_palindroma():
    lista = input_lista_int()

    if lista == lista[::-1]:
        print("Lista palindroma")
    else:
        print("Lista NON palindroma")


# =========================
# CONVERSIONI
# =========================

# Decimale -> Binario
def dec_bin():
    lista = input_lista_int()
    print([bin(x)[2:] for x in lista])


# Decimale -> Ottale
def dec_oct():
    lista = input_lista_int()
    print([oct(x)[2:] for x in lista])


# Decimale -> Esadecimale
def dec_hex():
    lista = input_lista_int()
    print([hex(x)[2:] for x in lista])


# Binario -> Decimale
def bin_dec():
    valori = input("Inserisci numeri binari separati da spazio: ").split()
    print([int(x, 2) for x in valori])


# Ottale -> Decimale
def oct_dec():
    valori = input("Inserisci numeri ottali separati da spazio: ").split()
    print([int(x, 8) for x in valori])


# Esadecimale -> Decimale
def hex_dec():
    valori = input("Inserisci numeri esadecimali separati da spazio: ").split()
    print([int(x, 16) for x in valori])


# Celsius -> Fahrenheit
def celsius_fahrenheit():
    lista = input_lista_float()
    print([(x * 9 / 5) + 32 for x in lista])


# Celsius -> Kelvin
def celsius_kelvin():
    lista = input_lista_float()
    print([x + 273.15 for x in lista])


# Ore -> Secondi
def ore_secondi():
    lista = input_lista_float()
    print([x * 3600 for x in lista])


# KM/H -> M/S
def kmh_ms():
    lista = input_lista_float()
    print([x / 3.6 for x in lista])


# HP -> KW
def hp_kw():
    lista = input_lista_float()
    print([x * 0.7457 for x in lista])


# Dizionario numeri romani
ROMANI = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


# Conversione numero romano
def numero_romano(n):

    risultato = ""

    for valore, simbolo in ROMANI.items():

        while n >= valore:
            risultato += simbolo
            n -= valore

    return risultato


# Decimale -> Romano
def dec_romani():
    lista = input_lista_int()
    print([numero_romano(x) for x in lista])


# =========================
# OPERAZIONI MATEMATICHE
# =========================

# Somma elementi lista
def somma_lista():
    lista = input_lista_float()
    print(sum(lista))


# Prodotto elementi lista
def prodotto_lista():
    lista = input_lista_float()
    print(reduce(lambda a, b: a * b, lista))


# Calcolo range
def range_lista():
    lista = input_lista_float()
    print(max(lista) - min(lista))


# Valore minimo
def minimo_lista():
    lista = input_lista_float()
    print(min(lista))


# Valore massimo
def massimo_lista():
    lista = input_lista_float()
    print(max(lista))


# Media matematica
def media_lista():
    lista = input_lista_float()
    print(sum(lista) / len(lista))


# Media ponderata
def media_ponderata():

    valori = input_lista_float()
    pesi = input_lista_float()

    totale = sum(v * p for v, p in zip(valori, pesi))

    print(totale / sum(pesi))


# Mediana
def mediana_lista():
    lista = input_lista_float()
    print(statistics.median(lista))


# Massimo comun divisore
def mcd_lista():
    lista = input_lista_int()
    print(reduce(gcd, lista))


# Calcolo minimo comune multiplo
def mcm(a, b):
    return abs(a * b) // gcd(a, b)


# MCM lista
def mcm_lista():
    lista = input_lista_int()
    print(reduce(mcm, lista))