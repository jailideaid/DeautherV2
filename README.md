# ⚡ Deauther V2 (Interactive Python Version)

Deauther V2 is a fully interactive terminal-based WiFi testing tool written in Python.  
It includes animated UI, ASCII art banners, interface selection, WiFi scanning, and manual deauthentication attack mode.

> ⚠️ **Educational Use Only**  
This tool is meant strictly for cybersecurity learning and authorized penetration testing.  
Do **NOT** use it on networks you do not own.

---

### 🚀 Features

✨ Modern animated terminal UI  
✨ ASCII banner with style  
✨ Auto interface detection (`iwconfig`)  
✨ Live WiFi scanning using `airodump-ng`  
✨ Manual target MAC input  
✨ Optional channel selection  
✨ Clean menu system with loading effects  
✨ Python3-based, easy to run anywhere

---


### 🔧 Requirements

The script needs:

### **System Tools**
- `aircrack-ng`
- `Wireless card with monitor mode support`
- `Python 3`

Install aircrack-ng (Debian/Ubuntu):

```
sudo apt update
sudo apt install aircrack-ng
```
---
### Python

Check Python 3:

`python3 --version`

---

### 🛠 Installation

1. Clone or download the project:

```
git clone https://github.com/youruser/DeautherV2.git
cd DeautherV2
```


2. (Optional) Make script executable:

`chmod +x deauther.py`

---
### ▶️ Running the Script

Run using:

`python3 deauther.py`

You will see:

- Animated banner

- Main menu

- Options to run a manual deauth attack
---

### 📜 Menu Options

1️⃣ Run Manual Deauth Attack

This option will:

1. Display your WiFi interfaces (iwconfig)

2. Ask for your interface (e.g., wlan0, wlx*)

3. Run WiFi scanner:

`airodump-ng <interface>`

4. Press CTRL + C when you see your target

5. Enter the Target MAC address

6. Enter the channel (optional)

7. Script launches:

`aireplay-ng -0 0 -a <MAC> <interface>`


0️⃣ Exit Program

Clean exit with animation.

---
### 🔍 Troubleshooting
Aircrack-ng not found

`
sudo apt install aircrack-ng
`

Interface not entering monitor mode

Use:

`sudo airmon-ng start <interface>`

Script not running

Check Python version:

`python3 --version`

Airodump permission error

Run with root:

`sudo python3 deauther.py`

---

### 📌 Disclaimer

This script is for learning and testing your own networks only.
Misuse may be illegal depending on your country.

---
### 🧧 Credits

Author: **Jail Idea**
Language: Python
Tools: Aircrack-ng Suite
Purpose: Ethical Hacking Learning

---
### ❤️ License

MIT License — free to modify, improve, and fork.
---
