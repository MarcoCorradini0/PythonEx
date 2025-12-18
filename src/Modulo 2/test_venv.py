# test_venv.py
# Script di verifica del corretto funzionamento dell'ambiente virtuale

import sys
import platform

print("=== Verifica ambiente virtuale ===")
print(f"Percorso interprete Python: {sys.executable}")
print(f"Versione Python: {platform.python_version()}")

# Verifica presenza pacchetti installati (requests come esempio)
try:
    import requests
    print(f"Modulo 'requests' disponibile, versione: {requests.__version__}")
except ImportError:
    print("Modulo 'requests' NON trovato. Installa con: pip install requests")

print("=== Fine test ===")
