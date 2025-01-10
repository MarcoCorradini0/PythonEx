#Chiedere all'utente da quale numero vuole calcolare la sequenza di Fibonacci, quanti numeri successivi vuole generare e poi stampare la sequenza.
#Funzione ricorsiva
def fibosequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibosequence(n-1) + fibosequence(n-2)

#Input utente
start=int(input("\nInserisci il numero da cui vuoi calcolare la sequenza di Fibonacci: "))
next=int(input("Inserisci quanti numeri vuoi generare: "))

#Stampa sequenza
for i in range(start, start+next):
    #stampa sequenza di Fibonacci separata da una virgola
    print(fibosequence(i), end=", " if i < start+next-1 else "\n")