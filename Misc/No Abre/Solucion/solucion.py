import zlib

data = bytes.fromhex("4948445200000380000002710802000000")
crc = zlib.crc32(data) & 0xffffffff
print(hex(crc))
