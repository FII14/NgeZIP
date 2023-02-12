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

print(f"""
#####################################
# d88888D d888888b d8888b. d888888b #
# YP  d8'   `88'   88  `8D   `88'   #
#    d8'     88    88oodD'    88    #
#   d8'      88    88~~~      88    #
#  d8' db   .88.   88        .88.   #
# d88888P Y888888P 88      Y888888P #
############### FII14 ###############
""")

file_zip = input("[»] Masukan nama file zip: ")
if(os.path.isfile(file_zip)):
    if file_zip.endswith(".zip"):
        time.sleep(1)
        file_wordlist = input("[»] Masukan nama file wordlist: ")
        if(os.path.isfile(file_wordlist)):
            with zipfile.ZipFile(file_zip, "r") as fz:
                with open(file_wordlist, "r") as fw:
                    for baris in fw:
                        kata_sandi = baris.strip()
                        try:
                            fz.extractall(pwd=bytes(kata_sandi, "utf-8"))
                            time.sleep(0.1)
                            print("[INFO]")
                            print("-------------- ISI FILE ZIP -------------")
                            for nama_file in fz.namelist():                             
                                print(f"[+] {nama_file}")
                            print("---------- KATA SANDI FILE ZIP ----------")
                            print(f"[+] {kata_sandi}")
                            print("-----------------------------------------\n")
                            break
                        except:
                            time.sleep(0.1)
                            print(f"[!] Mencoba kata sandi: {kata_sandi}")
                    else:
                        print(f"[INFO] Kata sandi tidak ditemukan dalam file wordlist {file_wordlist}.\n")
        else:
            time.sleep(3)
            print(f"[INFO] File {file_wordlist} tidak ditemukan.\n")
    else:
        time.sleep(3)
        print(f"[INFO] File {file_zip} bukan file zip.\n")
else:
    time.sleep(3)
    print(f"[INFO] File {file_zip} tidak ditemukan.\n")
