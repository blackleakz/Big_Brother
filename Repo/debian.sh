#!/bin/bash
# debian.sh

echo -e "Downloading requirements for debian!...."

repo = 'https://blackzspace.org/repo/Linux/'


cd ~
mkdir ~/BigBrother
cd ~/BigBrother

wget https://blackzspace.org/repo/Linux/requirements.txt
wget https://blackzspace.org/repo/Linux/change.log
