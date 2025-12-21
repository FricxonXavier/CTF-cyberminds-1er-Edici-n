import base64

# Cadena cifrada (la misma del reto)
cipher_b64 = "V15SU05yAlEDUAZpYQJEB0dlWQFfWGplBVFQB0ZFVwZfSQ=="

# Cargar diccionario (ajusta la ruta si es necesario)
with open("/usr/share/seclists/Passwords/Common-Credentials/500-worst-passwords.txt", "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f]

def xor_ps_style(b64_string: str, key: str) -> str:
    """
    Replica EXACTAMENTE:
    [System.Text.Encoding]::UTF8
    Base64 -> string UTF-8 -> bytes -> XOR -> string UTF-8
    """
    # Base64 -> bytes
    decoded_bytes = base64.b64decode(b64_string)

    # bytes -> string UTF-8 (como hace PowerShell)
    decoded_str = decoded_bytes.decode("utf-8", errors="ignore")

    data_bytes = decoded_str.encode("utf-8")
    key_bytes = key.encode("utf-8")

    out = bytearray()
    j = 0
    for i in range(len(data_bytes)):
        out.append(data_bytes[i] ^ key_bytes[j])
        j += 1
        if j >= len(key_bytes):
            j = 0

    return out.decode("utf-8", errors="ignore")

# Fuerza bruta de claves
for pwd in passwords:
    result = xor_ps_style(cipher_b64, pwd)
    if "flag" in result.lower() or "d3c0d3" in result.lower():
        print("[+] CLAVE:", pwd)
        print("[+] RESULTADO:", result)
        break
