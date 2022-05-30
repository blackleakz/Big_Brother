#!/bin/bash
# setup.sh

echo -n "Setup..."
sudo mkdir /usr/bin/BigBrother;
sudo mkdir /usr/bin/BigBrother/cli;
sudo mkdir /usr/bin/BigBrother/cli/logs;
cd /usr/bin/BigBrother
sudo rm -rf ./*
read -p "Press any key..."
sudo wget https://blackzspace.org/repo/Apps/BigBrother/main.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/mainwindow.py
sudo wget https://blackzspace.org/repo/Apps/BigBrother/terminalwindow.py

cd /usr/bin/BigBrother/cli
sudo wget https://blackzspace.org/repo/Apps/BigBrother/cli.py
cd /usr/bin/BigBrother

sudo ln -s /usr/bin/BigBrother/main.py ~/Desktop/BigBrother.py
sudo chmod 777 -R /usr/bin/BigBrother
sudo chmod 777 -R ~/Desktop/BigBrother.py

me="$(whoami)"
sudo chown $me -hR /usr/bin/BigBrother
sudo chown $me -hR ~/Desktop/BigBrother.py

echo -n "Installed at /usr/bin/BigBrother"
echo -e "Created shortcut."

sudo python3 /usr/bin/BigBrother/main.py
