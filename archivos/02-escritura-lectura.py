from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text()
print(texto)