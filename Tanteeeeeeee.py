import sys
import time
from colorama import Fore, Style, init

# inisialisasi colorama
init(autoreset=True)

def jalan_lirik():
    lirik = [
        ("temanku semua pada jahat tante", 0.1),
        ("aku lagi susah mereka gak ada", 0.1),
        ("coba kalau lagi jayaaa", 0.1),
        ("aku dipuja puja tantee", 0.1),
        ("sudah terbiasa terjadi tante", 0.1),
        ("teman datang ketika lagi butuh saja", 0.1),
        ("coba kalau lagi susaaahhh", 0.1),
        ("mereka semua menghilaaaaanggg", 0.1),
    ]

    delay = [1.1, 1.4, 1.3, 1.6, 1.25, 1.1, 1, 1.5]

    # ANSI code \033[1m = bold
    print(Fore.WHITE + "\033[1m\n--TAANNTEEEE--" + Style.RESET_ALL)
    time.sleep(3)

    for i, (baris_lagu, delay_char) in enumerate(lirik):
        for char in baris_lagu:
            print(Fore.GREEN + char + Style.RESET_ALL, end="")
            sys.stdout.flush()
            time.sleep(delay_char)
        time.sleep(delay[i])
        print("")

    print(Fore.WHITE + "// Code By Me" + Style.RESET_ALL)

jalan_lirik()