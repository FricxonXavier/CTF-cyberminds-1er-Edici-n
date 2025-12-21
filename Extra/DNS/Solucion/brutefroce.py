import base64

def rc4(key, data):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    out = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])

    return bytes(out)

cipher_b64 = "CU01h+7UmzsFXA+LAScdtQRrcxssJhs="
cipher = base64.b64decode(cipher_b64)

with open("/usr/share/wordlists/rockyou.txt", "r", errors="ignore") as f:
    for n, word in enumerate(f, 1):
        key = word.strip().encode()
        if not key:
            continue

        pt = rc4(key, cipher)

        if b"flag{" in pt:
            print("🔥 FLAG ENCONTRADA 🔥")
            print("Clave:", key.decode())
            print("Texto:", pt.decode())
            break

        if n % 200000 == 0:
            print("Probadas:", n)
