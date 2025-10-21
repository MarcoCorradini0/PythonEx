"""
ESERCIZIO 3: Problemi di Precisione Float
Obiettivo: Scoprire i limiti dei float
"""

# Stampiamo i float con 20 decimali per vedere la precisione
print("="*40)
print("PRECISIONE DEI FLOAT (20 decimali):")
print("="*40)

print(f"0.1 + 0.2 = {0.1 + 0.2:.20f}")
print(f"0.1 + 0.1 + 0.1 = {0.1 + 0.1 + 0.1:.20f}")
print(f"3 * 0.1 = {3 * 0.1:.20f}")

print("="*40)
print("CONFRONTI:")
print("="*40)

# Confronti che risultano TRUE
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)   # False a causa della precisione float
print("0.3 == 0.3:", 0.3 == 0.3)               # True
print("3 * 0.1 == 0.3:", 3 * 0.1 == 0.3)       # False per lo stesso motivo

# Confronti con tolleranza (usando math.isclose) per ottenere TRUE
import math

print("math.isclose(0.1 + 0.2, 0.3):", math.isclose(0.1 + 0.2, 0.3))
print("math.isclose(3 * 0.1, 0.3):", math.isclose(3 * 0.1, 0.3))

# Confronti che risultano FALSE
print("0.1 + 0.2 != 0.3:", 0.1 + 0.2 != 0.3) # True, perché la prima uguaglianza è False
print("3 * 0.1 != 0.3:", 3 * 0.1 != 0.3)     # True
