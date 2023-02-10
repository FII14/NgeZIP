# Program: Memecahkan kata sandi file zip
# Pembuat: FII14 

import zipfile
import os.path
import time
from colorama import Fore
b=Fore.LIGHTBLUE_EX
r=Fore.RESET
h=Fore.LIGHTGREEN_EX
k=Fore.LIGHTYELLOW_EX
m=Fore.LIGHTRED_EX
c=Fore.LIGHTCYAN_EX
p=Fore.LIGHTWHITE_EX
print(f"""{p}
#####################################
# {b}d88888D d888888b d8888b. d888888b {p}#
# {b}YP  d8'   `88'   88  `8D   `88'   {p}#
#    {b}d8'     88    88oodD'    88    {p}#
#   {b}d8'      88    88~~~      88    {p}#
#  {b}d8' db   .88.   88        .88.   {p}#
# {b}d88888P Y888888P 88      Y888888P {p}# 
############### {k}FII14 {p}###############
{r}""")
file_zip = input(f"{p}[{c}»{p}] {c}Masukan nama file zip{p}: {c}")
if(os.path.isfile(file_zip)):
    if file_zip.endswith(".zip"):
        time.sleep(1)
        file_wordlist = input(f"{p}[{c}»{p}] {c}Masukan nama file wordlist{p}: {c}")
        if(os.path.isfile(file_wordlist)):
            with zipfile.ZipFile(file_zip, "r") as fz:
                with open(file_wordlist, "r") as fw:
                    for baris in fw:
                        kata_sandi = baris.strip()
                        try:
                            fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                            time.sleep(1)
                            print(f"{p}[{h}INFO{p}] Kata sandi ditemukan{p}: {h}{kata_sandi}{r}\n")
                            break
                        except:
                            time.sleep(1)
                            print(f"{p}[{k}!{p}] {b}Mencoba kata sandi{p}: {k}{kata_sandi}{r}")
                    else:
                        print(f"{p}[{m}INFO{p}] {m}Kata sandi tidak ditemukan dalam file wordlist.{r}\n")
        else:
            time.sleep(3)
            print(f"{p}[{m}INFO{p}] {m}File {file_wordlist} tidak ditemukan.{r}\n")
    else:
        time.sleep(3)
        print(f"{p}[{m}INFO{p}] {m}File {file_zip} bukan file zip.{r}\n")
else:
    time.sleep(3)
    print(f"{p}[{m}INFO{p}] {m}File {file_zip} tidak ditemukan.{r}\n")
