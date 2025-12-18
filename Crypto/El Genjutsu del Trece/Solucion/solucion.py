def xor_string_with_int(input_string, xor_key):
    return ''.join([chr(ord(c) ^ xor_key) for c in input_string])

# Cadena hexadecimal obtenida del archivo
hex_string = "4b445e7647796e3c3d633e5e7e3d606f7f3970"

# Convertir de hexadecimal a bytes
ciphered_bytes = bytes.fromhex(hex_string)

# Decodificar a texto
ciphered_text = ciphered_bytes.decode('utf-8')

# Aplicar XOR con clave 13
xor_key = 13
decoded_flag = xor_string_with_int(ciphered_text, xor_key)

# Mostrar la flag
print(decoded_flag)
