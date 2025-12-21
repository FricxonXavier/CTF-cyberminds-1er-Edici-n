import re

ciphers = []

with open("log.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = re.search(r"PASSWORD:\s*([A-Za-z0-9+/=]+)", line)
        if m:
            ciphers.append(m.group(1))

ciphers = sorted(set(ciphers), key=len, reverse=True)

print("[+] Ciphertexts encontrados:", len(ciphers))
print("[+] Usando el más largo:")
print(ciphers[0])
import re

with open("DNS.log", "r") as f:
    for line in f:
        if "getdata.io" in line:
            print(line.strip())

