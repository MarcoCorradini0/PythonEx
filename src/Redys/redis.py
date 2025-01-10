#!/usr/bin/env python3

# inserimento di valori testuali associati a una chiave (stringa)
# visualizzazione di tutti i valori inseriti
# sovrascrittura di valori
# eliminazione di valori
# salvare su file tutte le informazioni inserite dall'utente

# Metodo per far inserire all'utente "nome cognome eta" e associarli ad una chiave
def inserimento() -> set:
    name = input("Inserisci il tuo nome: ")
    surname = input("Inserisci il tuo cognome: ")
    age = input("Inserisci la tua età: ")
    return {name, surname, age}
# Metodo salva su file il dict
def salva_su_file() -> None:
    with open("utenza.txt", "w") as f:
        f.write(str(inserimento()))
    f.close()
    
# Metodo per visualizzare i valori salvati nel file.txt
def visualizza() -> None:
    with open("utenza.txt", "r") as f:
        print(f.read())
    f.close()    

# Metodo sovrascrivi i valori nel file.txt
def sovrascrivi() -> None:
    with open("utenza.txt", "w") as f:
        f.write(str(inserimento()))
    f.close()

# Metodo per eliminare i valori nel file.txt
def elimina() -> None:
    with open("utenza.txt", "w") as f:
        f.write("")
    f.close()

# Menu principale
def menu() -> None:
    while True:
        print("\n1) Inserisci dati")
        print("2) Visualizza dati")
        print("3) Sovrascrivi dati")
        print("4) Elimina dati")
        print("5) Esci\n")
        scelta = input("Scelta: ")
        if scelta == "1":
            salva_su_file()
        elif scelta == "2":
            visualizza()
        elif scelta == "3":
            sovrascrivi()
        elif scelta == "4":
            elimina()
        elif scelta == "5":
            break
        else:
            print("Scelta non valida")
if __name__ == "__main__":
    menu()