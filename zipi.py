import zipfile

try:
    file_zip = input("Masukan nama file zip: ")

except FileNotFoundError:
    print("Kesalahan: file {file_zip} tidak ditemukan.")

else:
    try:
        wordlist_file = input("Masukan nama file wordlist: ")

    except FileNotFoundError:
        print(f"Kesalahan: file {wordlist_file} tidak ditemukan.")

    else:
        with zipfile.ZipFile(file_zip, "r") as fz:
            with open(file_woedlist, "r") as fw:
                for baris in fw:
                    kata_sandi = baris.strip()
                    try:
                        fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                        print(f"Kata sandi ditemukan: {kata_sandi}")
                        break
                    except:
                        print(f"Mencoba kata sandi: {kata_sandi}")
        print("Kata sandi tidak ditemukan dalam file wordlist.")

