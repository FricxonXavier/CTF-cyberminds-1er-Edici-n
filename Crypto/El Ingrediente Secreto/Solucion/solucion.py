#!/usr/bin/env python3
import os
import zipfile
import tarfile

def extract_files():
    while True:
        files = os.listdir(".")
        extracted = False

        for f in files:
            # ZIP
            if f.endswith(".zip"):
                print(f"[+] ZIP: {f}")
                with zipfile.ZipFile(f, 'r') as z:
                    z.extractall()
                os.remove(f)
                extracted = True

            # TAR
            elif f.endswith(".tar"):
                print(f"[+] TAR: {f}")
                with tarfile.open(f, 'r') as t:
                    t.extractall()
                os.remove(f)
                extracted = True

            # PDF camuflado como ZIP
            elif f.endswith(".pdf"):
                try:
                    os.rename(f, "temp.zip")
                    with zipfile.ZipFile("temp.zip", 'r') as z:
                        z.extractall()
                    os.remove("temp.zip")
                    extracted = True
                except:
                    os.rename("temp.zip", f)

        if not extracted:
            print("[✓] Extracción finalizada")
            break

if __name__ == "__main__":
    extract_files()
