# Configurazione Ambiente Python in Visual Studio Code
_Guida per macOS e Windows_

## 1. Requisiti
- Python 3.10+ installato  
  - macOS: già installato oppure scaricabile da python.org  
  - Windows: installare Python da python.org selezionando “Add Python to PATH”
- Visual Studio Code installato
- Estensione VS Code “Python” (Microsoft)

## 2. Creare la cartella di progetto
Scegli o crea una cartella locale, ad esempio:
```
progetto-python/
```
Aprila in Visual Studio Code.

## 3. Creare l’ambiente virtuale
### macOS
```
python3 -m venv .venv
```
### Windows
```
python -m venv .venv
```

## 4. Attivare l’ambiente virtuale
### macOS
```
source .venv/bin/activate
```
### Windows (PowerShell)
```
.venv\Scripts\activate
```

## 5. Selezionare l’interprete Python in VS Code
1. Cmd+Shift+P (macOS) / Ctrl+Shift+P (Win)
2. “Python: Select Interpreter”
3. Scegli quello dentro `.venv`

## 6. Verifica
```
python -c "import sys; print(sys.executable)"
pip install requests
python -c "import requests; print(requests.__version__)"
```

## 7. Disattivare
```
deactivate
```

## 8. Buone pratiche
- Un ambiente virtuale per ogni progetto.
- Non versionare `.venv` in Git.
