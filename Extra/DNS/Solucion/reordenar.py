import re
import base64

# 1️⃣ Extraer chunks
chunks = []
rx = re.compile(r"\[REQUEST\]\s+([A-Za-z0-9+/=]+)\.getdata\.io")

with open("DNS.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = rx.search(line)
        if m:
            chunks.append(m.group(1))

print("[+] Total chunks:", len(chunks))

# 2️⃣ Separar
data_chunks = chunks[:-4]
control_chunks = chunks[-4:]

print("[+] Data chunks:", len(data_chunks))
print("[+] Control chunks:", len(control_chunks))

# 3️⃣ Decodificar vector de orden
control = "".join(control_chunks)
control += "=" * ((-len(control)) % 4)

decoded = base64.b64decode(control).decode(errors="replace")
print("[+] Vector crudo:", decoded)

# Extraer números
order = list(map(int, re.findall(r"\d+", decoded)))
print("[+] Vector de orden:", order)
print("[+] Longitud vector:", len(order))

# 4️⃣ Reordenar los datos según el vector
reordered = []

for i in range(len(order)):
    idx = order.index(i)
    reordered.append(data_chunks[idx])

# Unir todo
final_b64 = "".join(reordered)

print("[+] Base64 reconstruido (inicio):", final_b64[:60])
print("[+] Longitud base64 final:", len(final_b64))

# 5️⃣ Decodificar Base64 y guardar ZIP
final_b64 += "=" * ((-len(final_b64)) % 4)

zip_bytes = base64.b64decode(final_b64)

with open("exfiltrated.zip", "wb") as f:
    f.write(zip_bytes)

print("[+] ZIP escrito como exfiltrated.zip")
print("[+] Magic bytes:", zip_bytes[:2])
