import os
import sys
import platform
import subprocess
import datetime
import configparser
import mainwindow
import terminalwindow
import PyQt5
import multiprocessing
import wget
import time
import os.path
import urllib.request
import requests
import socket
from threading import Thread
from os.path import exists

def init():
    os.system('cd /usr/bin/BigBrother/cli')
    os.system("mkdir logs")
    print("__________________________________________________________")
    print("||♠ BigBrother || (c) by BlackLeakz ||         | v.1.0 ™||")
    print("||------------------------------------------------------||")
    print("|| https://blackzspace.org/ |                           ||")
    print("__________________________________________________________")
    print("|| 1: netstat || 2: arp ||3: tracert || 4: ifconfig     ||")
    print("||------------------------------------------------------||")
    print("|| 5: tshark  || 6: whois   7: logs                     ||")
    print("__________________________________________________________")

    nr = input("Enter toolnr.:>")
    if nr == "1":
        netstat()

    if nr == "2":
        arp()
    if nr == "3":
        tracert()

    if nr == "4":
        ifconfig()

    if nr == '5':
        tshark()

    if nr == '6':
        whois()

    if nr == '7':
        logs()

def logs():
    subprocess.run(['ls', 'l', '/usr/bin/BigBrother/cli/logs'])
    d = input("Enter logfile 2 view:> ")
    os.system("cat " + d)
    input("press any key...")
    init()

def whois():
    os.system('whois -h')
    input("press any key...")
    y = input("Enter target: ")
    os.system('whois ' + y)
    input("press any key...")
    init()

def tshark():
    os.system("tshark -h")
    input("press any key...")
    os.system("ifconfig")
    input("press any key...")
    s = input("option:> ")
    os.system("sudo tshark " + s + " --log-file=/usr/bin/BigBrother/cli/logs/tshark.log")
    input("press any key...")
    init()

def netstat():
    os.system("netstat -h")
    input("press any key...")
    print("== v | a | l | t | r")
    x = input("option:> ")
    os.system('netstat -' + x)
    input("press any key...")
    init()

def ifconfig():
    os.system('ifconfig')
    input("press any key...")
    init()

def tracert():
    print("\n IPv4 : 4 || IPv6: 6")
    ipv = input("Enter protocol:> ")
    if ipv == "4":
        ip = input("Enter ip: ")
        ip = str(ip)
        os.system('traceroute -4 ' + ip)
        input("press any key...")
        init()

    if ipv == "6":
        ipy = input("Enter ip: ")

        os.system('traceroute -6 ' + ipy)
        input("press any key...")
        init()
    init()

def arp():
    os.system("arp -h")
    input("press any key...")
    os.system("arp -a")
    input("press any key...")
    init()


#def netstat():



def main():
    init()


if __name__ == '__main__':
    main()
