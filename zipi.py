import zipfile
import os.path
print("""
#####################################
# d88888D d888888b d8888b. d888888b #
# YP  d8'   `88'   88  `8D   `88'   #
#    d8'     88    88oodD'    88    #
#   d8'      88    88~~~      88    #
#  d8' db   .88.   88        .88.   #
# d88888P Y888888P 88      Y888888P # 
############### FII14 ###############
""")
file_zip = input("Masukan nama file zip: ")
if(os.path.isfile(file_zip)):
    if file_zip.endswith(".zip"):
        file_wordlist = input("Masukan nama file wordlist: ")
        if(os.path.isfile(file_wordlist)):
            with zipfile.ZipFile(file_zip, "r") as fz:
                with open(file_wordlist, "r") as fw:
                    for baris in fw:
                        kata_sandi = baris.strip()
                        try:
                            fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                            print(f"[INFO] Kata sandi ditemukan: {kata_sandi}\n")
                            break
                        except:
                            print(f"Mencoba kata sandi: {kata_sandi}")
                    else:
                        print("Kata sandi tidak ditemukan dalam file wordlist.\n")
        else:
            print(f"File {wordlist_file} tidak ditemukan.\n")
    else:
        print(f"File {file_zip} bukan file zip.\n")
else:
    print(f"File {file_zip} tidak ditemukan.\n")
