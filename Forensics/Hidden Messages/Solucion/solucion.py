import base64

b64 = "JTAxHiEZG1lQHm53Vw1WOicDBV4HGAJXPEtSV0cQ"
data = base64.b64decode(b64)

key = "cyberminds13"

def xor_with_key(data, key):
    key = key.encode()
    return bytes(
        b ^ key[i % len(key)]
        for i, b in enumerate(data)
    )

flag_bytes = xor_with_key(data, key)
print(flag_bytes)
print(flag_bytes.decode())
