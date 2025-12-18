import base64

with open("message1.txt", "r") as fin, open("b32decode.txt", "w") as fout:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        line += "=" * (-len(line) % 8)
        decoded = base64.b32decode(line)
        fout.write(decoded.decode("utf-8", errors="ignore"))
