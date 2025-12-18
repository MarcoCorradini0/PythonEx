# Utilizzo e Attivazione di un Ambiente Virtuale Python da Visual Studio Code

## 1. Prerequisiti
- Python 3.10+ installato
- Visual Studio Code
- Estensione “Python” (Microsoft)
- Una cartella di progetto contenente un ambiente virtuale `.venv`

---

## 2. Creare l’ambiente virtuale da Visual Studio Code
Apri il terminale integrato:

```
Terminal → New Terminal
```

### macOS
```
python3 -m venv .venv
```

### Windows
```
python -m venv .venv
```

---

## 3. Attivare l’ambiente virtuale direttamente da VS Code

### macOS
Nel terminale integrato:
```
source .venv/bin/activate
```

### Windows (PowerShell):
```
.venv\Scripts\activate
```

Dopo l’attivazione il terminale mostrerà:
```
(.venv) ...
```

---

## 4. Impostare automaticamente l’ambiente virtuale in VS Code
Visual Studio Code può selezionare automaticamente l’interprete Python dentro `.venv`.

Procedura:
1. Apri la *Command Palette*  
   - macOS: Cmd + Shift + P  
   - Windows: Ctrl + Shift + P
2. Cerca:  
   ```
   Python: Select Interpreter
   ```
3. Seleziona l’interprete associato al percorso `.venv`.

Dopo questa scelta, VS Code userà automaticamente il venv per:  
- Esecuzione script  
- Debug  
- Terminale integrato  
- IntelliSense / Linting  
- Installazione pacchetti con pip

---

## 5. Attivazione automatica del venv nei terminali di VS Code
Se l’interprete è impostato correttamente, aprendo un nuovo terminale VS Code tenterà di attivare l’ambiente virtuale in automatico.  
Se non lo fa, verifica il file:

```
.vscode/settings.json
```

E assicurati che contenga:

```json
{
    "python.defaultInterpreterPath": ".venv/bin/python"
}
```

Per Windows:

```json
{
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}
```

---

## 6. Verifica del corretto funzionamento
Nel terminale attivo:

```
python -c "import sys; print(sys.executable)"
```

Il percorso deve terminare con:

- `.venv/bin/python` su macOS  
- `.venv\Scripts\python.exe` su Windows

---

## 7. Disattivare l’ambiente virtuale
```
deactivate
```

---

## 8. Nota per gli studenti
Usate sempre l’ambiente virtuale per:
- Separare i pacchetti tra progetti diversi  
- Evitare conflitti di versione  
- Avere un setup pulito e riproducibile  

