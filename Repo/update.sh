#!/bin/bash
# update.sh
# Version 1.1

echo -n "Updating..."



sudo mkdir /usr/bin/BigBrother/.old
sudo mv /usr/bin/BigBrother/* /usr/bin/BigBrother/.old

cd /usr/bin/BigBrother

sudo wget https://blackzspace.org/repo/Apps/BigBrother/main.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/mainwindow.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/cli.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/terminalwindow.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/update.sh
sudo wget https://blackzspace.org/repo/Apps/BigBrother/setup.sh
sudo wget https://blackzspace.org/repo/Apps/BigBrother/requirements.txt
sudo pkill python

sudo python3 main.py;
