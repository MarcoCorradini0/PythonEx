# Utilizzare i Notebook Jupyter in Visual Studio Code
_Guida rapida per studenti (macOS e Windows)_

Questa guida spiega come creare e usare i notebook Jupyter direttamente dentro Visual Studio Code, usando l’ambiente virtuale `.venv` del progetto.

---

## 1. Prerequisiti

- **Python 3.10+** installato
- **Visual Studio Code** installato
- Estensioni VS Code:
  - **Python** (Microsoft)
  - **Jupyter** (Microsoft)
- Un progetto già configurato con ambiente virtuale `.venv` (vedi guida dedicata)

---

## 2. Installare le estensioni necessarie

1. Apri Visual Studio Code.
2. Vai alla sezione **Extensions** (icona a sinistra oppure `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Cerca e installa:
   - `Python` (autore: Microsoft)
   - `Jupyter` (autore: Microsoft)

Assicurati che entrambe le estensioni risultino **Installed** e **Enabled**.

---

## 3. Creare un nuovo Notebook Jupyter

Hai due possibilità:

### Opzione A – Dal Command Palette
1. Apri il **Command Palette**:
   - macOS: `Cmd + Shift + P`
   - Windows: `Ctrl + Shift + P`
2. Digita:
   ```
   Jupyter: Create New Jupyter Notebook
   ```
3. Salva il file con estensione:
   ```
   .ipynb
   ```

### Opzione B – Da un file esistente
1. Crea un nuovo file:
   ```
   File → New File
   ```
2. Salva il file con estensione:
   ```
   nome_file.ipynb
   ```
3. VS Code lo aprirà automaticamente in modalità Notebook.

---

## 4. Selezionare il Kernel (ambiente di esecuzione)

Il *kernel* è l’interprete Python che esegue le celle del notebook.  
Dobbiamo assicurarci che il notebook usi **l’ambiente virtuale `.venv`** del progetto.

1. In alto a destra nel notebook, clicca sul nome del kernel (es. “Python 3.x” o “Select Kernel”).
2. Seleziona:
   - **Python Environments**
   - Scegli l’interprete che punta alla cartella `.venv` del progetto:
     - macOS: percorso che termina con `.venv/bin/python`
     - Windows: percorso che termina con `.venv\Scripts\python.exe`

Se il `.venv` non compare:
- Verifica di averlo creato nella cartella del progetto.
- Assicurati di aver aperto la cartella corretta in VS Code.

---

## 5. Struttura di base di un Notebook

Un notebook è composto da **celle**.  
Esistono due tipi principali:

- **Code cell**: contiene codice Python
- **Markdown cell**: contiene testo formattato (titoli, elenchi, descrizioni, formule)

Per aggiungere una cella:
- Usa il pulsante `+ Code` o `+ Markdown` nella barra del notebook.
- Oppure usa le scorciatoie (vedi paragrafo 7).

---

## 6. Eseguire il codice nel Notebook

### Eseguire una singola cella
- Clicca sull’icona “Play” (▶) a sinistra della cella, oppure
- Usa la scorciatoia:
  - macOS: `Shift + Enter`
  - Windows: `Shift + Enter`

Il risultato apparirà sotto la cella.

### Eseguire tutte le celle
- In alto nella barra del notebook:
  - `Run All` (Esegui tutto)

---

## 7. Scorciatoie utili nei Notebook

(Le scorciatoie possono variare a seconda delle impostazioni, ma in genere:)

- **Eseguire cella e passare alla successiva**: `Shift + Enter`
- **Aggiungere una cella sotto**: `B`
- **Aggiungere una cella sopra**: `A`
- **Convertire cella in codice**: `Y`
- **Convertire cella in markdown**: `M`
- **Cancellare cella**: `D` + `D` (premere `D` due volte)

Nota: alcune scorciatoie funzionano quando il notebook è in **command mode** (contorno blu); per entrarci, premi `Esc`.  
Per tornare in **edit mode** (contorno verde), premi `Enter` dentro la cella.

---

## 8. Salvare, chiudere e riaprire un Notebook

- Per salvare:  
  `File → Save` oppure `Ctrl + S` (Windows) / `Cmd + S` (macOS).
- I file vengono salvati con estensione:
  ```
  .ipynb
  ```
- Per riaprire un notebook, fai doppio click sul file `.ipynb` in Explorer (barra laterale di sinistra).

---

## 9. Utilizzare i pacchetti nel Notebook

I notebook usano gli stessi pacchetti installati nell’ambiente virtuale selezionato come kernel.

Esempio:

1. Nel terminale del progetto (con `.venv` attivo):
   ```bash
   pip install numpy pandas matplotlib
   ```
2. Nel notebook:
   ```python
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   ```

Se ottieni errori di `ModuleNotFoundError`, verifica:
- Che il kernel selezionato sia quello di `.venv`
- Che i pacchetti siano stati installati **dentro** `.venv` e non globalmente

---

## 10. Esportare un Notebook

Visual Studio Code permette di esportare il notebook in altri formati.

1. Apri il notebook `.ipynb`.
2. In alto a destra, clicca sui tre puntini `…`.
3. Seleziona una delle opzioni, ad esempio:
   - `Export As → HTML`
   - `Export As → PDF` (se configurato)
   - `Export As → Python Script` (`.py`)

La versione `.py` è utile se volete trasformare il notebook in uno script Python lineare.

---

## 11. Buone pratiche per gli studenti

- Usate un notebook per:
  - Esercizi passo-passo
  - Esempi di codice con spiegazione
  - Esperimenti con dati (pandas, grafici, ecc.)
- Commentate bene il codice usando:
  - Celle **Markdown** per teoria/spiegazioni
  - Celle **Code** per il codice effettivo
- Mantenete i notebook organizzati in cartelle (es. `lezione_01`, `lezione_02`, ecc.).
- Per progetti veri e propri, affiancate al notebook anche file `.py`.

---

Se necessario, questo documento può essere adattato in versione:
- Ultra-sintetica per slide
- Handout di una sola pagina
- Guida con screenshot passo-passo
