import re
import base64

# 1️⃣ Leer el log y extraer los subdominios
chunks = []

rx = re.compile(r"\[REQUEST\]\s+([A-Za-z0-9+/=]+)\.getdata\.io")

with open("DNS.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = rx.search(line)
        if m:
            chunks.append(m.group(1))

print("[+] Total chunks encontrados:", len(chunks))

# 2️⃣ Tomar los últimos 4 (bloque de control)
control = "".join(chunks[-4:])

# Arreglar padding base64 si falta
control += "=" * ((-len(control)) % 4)

# 3️⃣ Decodificar
decoded = base64.b64decode(control)

print("[+] Control decodificado:")
print(decoded.decode(errors="replace"))
