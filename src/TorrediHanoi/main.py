import tkinter as tk

def start_gui(n):
   global root, canvas, towerpos, torri, selected_tower, selected_disk, move_count, min_moves, mosse, disk
   # Crea la finestra principale
   root = tk.Tk()
   root.title("Torre di Hanoi")

   # Menu di gioco (con il comando per risolvere il gioco)
   menu = tk.Menu(root)
   root.config(menu=menu)
   game_menu = tk.Menu(menu, tearoff=0)
   menu.add_cascade(label="Gioco", menu=game_menu)
   game_menu.add_command(label="Risolvi", command=soluzione)

   # Crea un'area di disegno (Canvas)
   canvas = tk.Canvas(root, width=1000, height=600)
   canvas.pack()
   
   # Posizioni delle 3 torri (A, B, C) sullo schermo
   towerpos = [100, 300, 500]
   for i in range(3):
       # Disegna le torri come rettangoli
       canvas.create_rectangle(towerpos[i] - 20, 50, towerpos[i] + 20, 350, fill="gray")
   
   # Crea i dischi e li organizza in base alla quantità di dischi (n)
   disk = []
   for i in range(n, 0, -1):
       disk_width = 20 + i * 40  # Larghezza dei dischi in base al numero
       disk.append(disk_width)
   
   # Stato iniziale delle torri: torre A ha tutti i dischi, B e C sono vuote
   torri = {'A': [], 'B': disk.copy(), 'C': []}
   selected_tower = None
   selected_disk = None
   move_count = 0
   min_moves = 2 ** n - 1  # Calcola il numero minimo di mosse necessarie per vincere
   print_disks()  # Mostra i dischi sullo schermo
   
   # Mostra le mosse minime necessarie
   mosse = tk.Label(root, text=f"Mosse minime necessarie: {min_moves}")
   mosse.pack(pady=10)
   
   # Assegna un evento per cliccare sui dischi
   canvas.bind("<Button-1>", on_click)
   root.mainloop()  # Avvia il loop principale dell'interfaccia grafica

def print_disks():
    global towerpos, torri
    canvas.delete("all")  # Pulisce il canvas prima di ridisegnare le torri e i dischi

    # Ridisegna le torri
    for i in range(3):
        canvas.create_rectangle(towerpos[i] - 20, 50, towerpos[i] + 20, 350, fill="gray")
    
    # Disegna i dischi sopra le torri, con colori diversi per ogni disco
    for i, tower in enumerate(['A', 'B', 'C']):
        y = 350
        for disk_width in torri[tower]:
            # Colorazione dei dischi con un gradiente di colori
            red = (disk_width * 3) % 256
            green = (disk_width * 5) % 256
            blue = (disk_width * 7) % 256
            color = f"#{red:02x}{green:02x}{blue:02x}"  # Formatta il colore come stringa esadecimale
            canvas.create_rectangle(
                towerpos[i] - disk_width // 2, y - 20,
                towerpos[i] + disk_width // 2, y,
                fill=color
            )
            y -= 20  # Sposta ogni disco sopra l'altro

def on_click(event):
    global selected_disk, selected_tower, torri, move_count, min_moves, mosse
    clicked_tower = None

    # Verifica su quale torre è stato cliccato
    if event.x < towerpos[0] + 20 and event.x > towerpos[0] - 20:
        clicked_tower = 'A'
    elif event.x < towerpos[1] + 20 and event.x > towerpos[1] - 20:
        clicked_tower = 'B'
    elif event.x < towerpos[2] + 20 and event.x > towerpos[2] - 20:
        clicked_tower = 'C'

    # Se una torre è stata cliccata, esegui le azioni
    if clicked_tower:
        if selected_disk is None:
            # Se non c'è un disco selezionato, seleziona l'ultimo disco della torre cliccata
            if torri[clicked_tower]:
                selected_tower = clicked_tower
                selected_disk = torri[clicked_tower][-1]
                print_disks()
        else:
            # Se c'è già un disco selezionato, prova a spostarlo nella torre cliccata
            if clicked_tower != selected_tower:
                if not torri[clicked_tower] or torri[clicked_tower][-1] > selected_disk:
                    # Sposta il disco dalla torre selezionata alla torre cliccata
                    torri[selected_tower].remove(selected_disk)
                    torri[clicked_tower].append(selected_disk)
                    selected_disk = None
                    selected_tower = None
                    move_count += 1
                    mosse.config(text=f"Movimenti fatti: {move_count}")
                    print_disks()
                    
                    # Verifica se l'utente ha vinto
                    if torri['C'] == sorted(torri['C'], reverse=True) and len(torri['C']) == len(disk):
                        mosse.config(text=f"Hai vinto! Mosse fatte: {move_count}")
            else:
                # Deselect il disco se si clicca sulla stessa torre
                selected_disk = None
                selected_tower = None
                print_disks()

def action(from_t, to_t):
    global torri
    # Esegui il movimento di un disco da una torre a un'altra
    if torri[from_t]:
        disk = torri[from_t].pop()
        torri[to_t].append(disk)
        print_disks()

def sequence(moves):
    # Esegui una sequenza di mosse per risolvere il gioco
    for from_t, to_t in moves:
        action(from_t, to_t)
        root.update_idletasks()  # Aggiorna l'interfaccia grafica
        root.after(500)  # Aspetta mezzo secondo tra le mosse

def logica(n, from_t, to_t, aux_t, moves):
    # Funzione ricorsiva per generare la sequenza ottimale di mosse
    if n == 1:
        moves.append((from_t, to_t))
        return
    logica(n-1, from_t, aux_t, to_t, moves)  # Muovi i dischi n-1 alla torre ausiliaria
    moves.append((from_t, to_t))  # Muovi l'ultimo disco alla torre finale
    logica(n-1, aux_t, to_t, from_t, moves)  # Muovi i dischi n-1 alla torre finale

def torre_moves(n):
    # Calcola la sequenza di mosse ottimale per risolvere il gioco
    moves = []
    logica(n, 'A', 'C', 'B', moves)
    return moves

def soluzione():
    # Esegui la sequenza di mosse ottimali per risolvere il gioco
    moves = torre_moves(len(torri['A']))
    sequence(moves)

def num_disks():
    def start_game():
        try:
            # Prendi il numero di dischi dal campo di input
            n = int(entry.get())
            if n < 1:
                error_label.config(text="Inserisci un numero positivo")
            else:
                root.destroy()
                start_gui(n)  # Inizia il gioco con il numero di dischi scelto
        except ValueError:
            error_label.config(text="Inserisci un numero valido")
    
    # Crea la finestra di input per il numero di dischi
    root = tk.Tk()
    root.title("Torre di Hanoi")
    prompt_label = tk.Label(root, text="Inserisci il numero di dischi:")
    prompt_label.pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=10)
    start_button = tk.Button(root, text="Inizia", command=start_game)
    start_button.pack(pady=10)
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)
    root.mainloop()

# Avvia il gioco
num_disks()
