import base64

cipher_b64 = "EyUnCTEXIzw4UCsoFwBRYlwrAlViCx4="
key = "UltraSecretKey!"

cipher = base64.b64decode(cipher_b64)

out = ""
for i in range(len(cipher)):
    out += chr(cipher[i] ^ ord(key[i % len(key)]))

print("FLAG DECODIFICADA:", out)
