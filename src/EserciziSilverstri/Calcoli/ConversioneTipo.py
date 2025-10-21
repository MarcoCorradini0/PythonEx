"""
ESERCIZIO 2: Conversioni di Tipo
Obiettivo: Praticare casting tra tipi
"""

# Conversioni

# Da float a intero (troncamento della parte decimale)
int_da_float = int(12.75)

# Da intero a float
float_da_intero = float(12)

# Da intero a stringa
stringa_da_intero = str(123)

# Da stringa a intero (se la stringa contiene un numero valido)
intero_da_stringa = int("456")

# Da intero a booleano (0 è False, qualsiasi altro valore è True)
bool_da_intero = bool(0)    # False
bool_da_intero2 = bool(42)  # True

# Da float a stringa
stringa_da_float = str(3.14)

# Da booleano a intero (False -> 0, True -> 1)
int_da_bool = int(True)

# Da booleano a zero (stesso concetto di sopra, False è zero)
bool_da_zero = bool(0)  # False

# Stampiamo i risultati
print("int_da_float:", int_da_float)
print("float_da_intero:", float_da_intero)
print("stringa_da_intero:", stringa_da_intero)
print("intero_da_stringa:", intero_da_stringa)
print("bool_da_intero (0):", bool_da_intero)
print("bool_da_intero (42):", bool_da_intero2)
print("stringa_da_float:", stringa_da_float)
print("int_da_bool (True):", int_da_bool)
print("bool_da_zero (0):", bool_da_zero)