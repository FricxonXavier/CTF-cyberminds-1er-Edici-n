import re

chunks = []

rx = re.compile(r"\[REQUEST\]\s+([A-Za-z0-9+/=]+)\.getdata\.io")

with open("DNS.log") as f:
    for line in f:
        m = rx.search(line)
        if m:
            chunks.append(m.group(1))

print("Total chunks:", len(chunks))
print("Primeros 5:", chunks[:5])
print("Últimos 5:", chunks[-5:])
