#!/bin/sh
# arch.sh

echo -n "Installing dependencies..."

cd ~
mkdir ~/BigBrother
cd ~/BigBrother
sudo pacman -Syy wget;
sudo wget https://blackzspace.org/repo/Linux/requirements.txt
sudo wget https://blackzspace.org/repo/Linux/change.log

sudo pacman -Syyuu;
sudo pacman -Syy make cmake bash-completion;
sudo pacman -Syy git nmap whois;
sudo pacman -Syy iproute2 aircrack-ng traceroute;
sudo pacman -Syy metasploit;
sudo pacman -Syy wireshark-qt;
