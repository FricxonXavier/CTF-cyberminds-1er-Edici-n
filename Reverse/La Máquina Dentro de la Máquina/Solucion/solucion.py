KEY = 0x5A

def run_vm(enc):
    regs = [0, 0, 0, 0]
    pc = 0
    out = []

    while pc < len(enc):
        op = enc[pc] ^ KEY
        pc += 1

        if op == 0x01:  # LOADI
            if pc + 1 >= len(enc):
                break
            r = (enc[pc] ^ KEY) & 0x03
            pc += 1
            imm = enc[pc] ^ KEY
            pc += 1
            regs[r] = imm

        elif op == 0x05:  # PRINT
            if pc >= len(enc):
                break
            r = (enc[pc] ^ KEY) & 0x03
            pc += 1
            out.append(chr(regs[r]))

        elif op == 0xFF:  # HALT
            break
        else:
            break

    return "".join(out)

if __name__ == "__main__":
    with open("enc.bin", "rb") as f:
        enc = f.read()

    print("Flag:", run_vm(enc))
