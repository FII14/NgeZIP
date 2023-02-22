# Program: Memecahkan kata sandi file zip
# Pembuat: FII14

###################################################################################################################################
# Lisensi MIT                                                                                                                     #
#                                                                                                                                 #
# Hak Cipta (c) 2023 FII14                                                                                                        #
#                                                                                                                                 #
# Dengan ini diberikan izin, secara gratis, kepada siapa pun yang mendapatkan salinan                                             #
# perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak"), untuk bertransaksi                                        #
# dalam Perangkat Lunak tanpa batasan, termasuk namun tidak terbatas pada hak                                                     #
#                                                                                                                                 #          
# untuk menggunakan, menyalin, memodifikasi, menggabungkan, mempublikasikan, mendistribusikan, mensublisensikan, dan/atau menjual #
# salinan Perangkat Lunak, dan untuk mengizinkan orang yang menerima Perangkat Lunak.                                             #
# yang diberikan Perangkat Lunak untuk melakukan hal tersebut, dengan tunduk pada ketentuan-ketentuan berikut:                    #
#                                                                                                                                 #
# Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua                                         #
# salinan atau bagian penting dari Perangkat Lunak.                                                                               #
#                                                                                                                                 #
# PERANGKAT LUNAK INI DISEDIAKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN APA PUN, TERSURAT MAUPUN                                     #
# TERSURAT MAUPUN TERSIRAT, TERMASUK NAMUN TIDAK TERBATAS PADA JAMINAN DAPAT DIPERJUALBELIKAN,                                    #
# KESESUAIAN UNTUK TUJUAN TERTENTU DAN NON-PELANGGARAN. DALAM HAL APA PUN                                                         #
# PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN, ATAU                                             #
# TANGGUNG JAWAB, BAIK DALAM TINDAKAN KONTRAK, KESALAHAN ATAU LAINNYA, YANG TIMBUL DARI,                                          #
# DARI ATAU SEHUBUNGAN DENGAN PERANGKAT LUNAK ATAU PENGGUNAAN ATAU TRANSAKSI LAIN DALAM                                           #
# PERANGKAT LUNAK.                                                                                                                #
###################################################################################################################################

import zipfile
import os.path
import time
import os
from colorama import Fore as f

m=f.LIGHTRED_EX
p=f.LIGHTWHITE_EX
k=f.LIGHTYELLOW_EX
r=f.RESET
b=f.LIGHTBLUE_EX
c=f.LIGHTCYAN_EX
h=f.LIGHTGREEN_EX

os.system("clear")

print(f"""
{m} _   _  ____ _____ ________ ____   {r}{k} 
{m}| \ | |/ ___| ____|__  /_ _|  _ \  {r}{k}Program {r}| {k}Memecahkan kata sandi file zip{r}
{m}|  \| | |  _|  _|   / / | || |_) | {r}{k}Pembuat {r}| {k}Rofi{r}
{p}| |\  | |_| | |___ / /_ | ||  __/  {r}{k}Github  {r}| {k}https://github.com/FII14/ngezip{r}
{p}|_| \_|\____|_____/____|___|_|     {r}{k}E-mail  {r}| {k}rofikun14122003@gmail.com{r}
""")

file_zip = input(f"{p}[{b}»{p}] Masukan nama file zip: ")
if(os.path.isfile(file_zip)):
    if file_zip.endswith(".zip"):
        time.sleep(1)
        file_wordlist = input(f"{p}[{b}»{p}] Masukan nama file wordlist: ")
        if(os.path.isfile(file_wordlist)):
            with zipfile.ZipFile(file_zip, "r") as fz:
                with open(file_wordlist, "r") as fw:
                    for baris in fw:
                        kata_sandi = baris.strip()
                        try:
                            fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                            time.sleep(0.1)
                            print(f"{p}[{c}INFO{p}]{r}")
                            print(f"{p}-------------- {h}ISI FILE ZIP {p}-------------{r}")
                            for nama_file in fz.namelist():                             
                                print(f"{p}[{h}+{p}] {nama_file}{r}")
                            print(f"{p}---------- {h}KATA SANDI FILE ZIP {p}----------{r}")
                            print(f"{p}[{h}+{p}] {kata_sandi}{r}")
                            print(f"{p}-----------------------------------------{r}\n")
                            break
                        except:
                            time.sleep(0.1)
                            print(f"{p}[{m}!{p}] {k}Mencoba kata sandi{r}: {m}{kata_sandi}{r}")
                    else:
                        print(f"{p}[{c}INFO{p}] {m}Kata sandi tidak ditemukan dalam file wordlist {file_wordlist}.{r}\n")
        else:
            time.sleep(3)
            print(f"{p}[{c}INFO{p}] {m}File {file_wordlist} tidak ditemukan.{r}\n")
    else:
        time.sleep(3)
        print(f"{p}[{c}INFO{p}] {m}File {file_zip} bukan file zip.{r}\n")
else:
    time.sleep(3)
    print(f"{p}[{c}INFO{p}] {m}File {file_zip} tidak ditemukan.{r}\n")
