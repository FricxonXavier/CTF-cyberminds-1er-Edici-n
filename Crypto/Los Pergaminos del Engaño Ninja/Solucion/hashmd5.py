import hashlib
import string

# Archivo con hashes MD5 (uno por línea)
FILE = "b32decode.txt"

# Conjunto de caracteres a probar (ajusta si es necesario)
charset = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation +
    " "
)

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

decoded = ""

with open(FILE, "r") as f:
    for line in f:
        hash_line = line.strip()
        found = False

        for c in charset:
            if md5(c) == hash_line:
                decoded += c
                found = True
                break

        if not found:
            decoded += "?"

print("Frase decodificada:")
print(decoded)
