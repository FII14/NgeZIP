import zipfile
import os.path


file_zip = input("Masukan nama file zip: ")

if(os.path.isfile(file_zip)):
    file_wordlist = input("Masukan nama file wordlist: ")

    if(os.path.isfile(file_wordlist)):
        
        try:
            with zipfile.ZipFile(file_zip, "r") as fz:
                with open(file_wordlist, "r") as fw:
                    for baris in fw:
                        kata_sandi = baris.strip()
                        try:
                            fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                            print(f"Kata sandi ditemukan: {kata_sandi}")
                            break
                        except:
                            print(f"Mencoba kata sandi: {kata_sandi}")
                    else:
                        print("Kata sandi tidak ditemukan dalam file wordlist.")

        except zipfile.BadZipFile:
            print(f"File {file_zip} bukan file zip.")

    else:
        print(f"File {wordlist_file} tidak ditemukan.")

else:
    print(f"File {file_zip} tidak ditemukan.")
