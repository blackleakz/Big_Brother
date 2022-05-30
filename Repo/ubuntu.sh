#!/bin/bash
# ubuntu.sh

echo -e "Downloading requirements for ubuntu!...."

repo = 'https://blackzspace.org/repo/Linux/'


cd ~
mkdir ~/BigBrother
cd ~/BigBrother

wget https://blackzspace.org/repo/Linux/requirements.txt
wget https://blackzspace.org/repo/Linux/change.log
