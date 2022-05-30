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
import keyboard
from threading import Thread
from os.path import exists
from mainwindow import *
from terminalwindow import *
from PyQt5 import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.progressBar.setProperty("value", 0)
        date = datetime.datetime.now()
        date = str(date)
        self.terminalBrowser.append("Date: " + date)
        self.terminalBrowser.append("  ♠ BigBrother || (c) by BlackLeakz || Windows | v.1.0 ™")
        self.terminalBrowser.append("\n")
        self.terminalBrowser.append("==== https://blackzspace.org/ ==========================")
        self.terminalBrowser.append("\n")
        os.system('cd /usr/bin/BigBrother')

    def checkstatus(self):
        a_socket = socket.socket()

        try:
            a_socket.connect(("217.160.54.61", 80))
            self.terminalBrowser.append("Online...")
            self.status.setText("Online")
            print("online")
        except:
            self.terminalBrowser.append("Connection failed.")
            print("Connection failed")

    def update(self):
        self.terminalBrowser.append("\n Updating...")
        def bar_custom(current, total, width=80):
            print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
            self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

        repourl = 'https://blackzspace.org/repo/Linux/update.sh'
        write_file = 'update.sh'
        wget.download(repourl, write_file, bar=bar_custom)
        if os.path.isfile('update.sh'):
            print('|| update.sh exist!  ')
            self.terminalBrowser.append('|| update.sh exist! ')
            os.system("sudo rm update.sh")
            wget.download(repourl, write_file, bar=bar_custom)
            os.system("sudo sh update.sh")
        else:
            print('|| update.sh dosent exist!!')
            self.terminalBrowser.append('|| update.sh dosent exist!')
            wget.download(repourl, write_file, bar=bar_custom)
            os.system("sudo sh update.sh")



    def autoconf(self):
        self.progressBar.setProperty("value", 0)
        date = datetime.datetime.now()
        date = str(date)
        plat = platform.system()
        print(date + "|| Detecting OS type...")
        print(date + '|| System   :', platform.system())
        print(date + '|| Node     :', platform.node())
        print(date + '|| Release  :', platform.release())
        print(date + '|| Version  :', platform.version())
        print(date + '|| Machine  :', platform.machine())
        print(date + '|| Processor:', platform.processor())
        sys = platform.system()
        node = platform.node()
        rel = platform.release()
        ver = platform.version()
        mach = platform.machine()
        proc = platform.processor()

        self.terminalBrowser.append(date + '|| System   : ' + sys)
        self.terminalBrowser.append(date + '|| Node     : ' + node)
        self.terminalBrowser.append(date + '|| Release  : ' + rel)
        self.terminalBrowser.append(date + '|| Version  : ' + ver)
        self.terminalBrowser.append(date + '|| Machine  : ' + mach)
        self.terminalBrowser.append(date + '|| Processor: ' + proc)
        self.progressBar.setProperty("value", 30)

        if plat == "Windows":
            self.progressBar.setProperty("value", 40)
            date = datetime.datetime.now()
            date = str(date)
            print(date + "|| Configuring app for your Windows-System...|><|..|<>|..|><|.")
            self.terminalBrowser.append(date + "|| Configuring app for your Windows-System...|><|..|<>|..|><|.")
            oscwd = os.getcwd()

            pathx = os.path.abspath(__file__)
            print(date + '|| Scriptfile :' + pathx)
            print(date + '|| Working-dircetory: ' + oscwd)
            self.terminalBrowser.append(date + '|| Scriptfile: ' + pathx)
            self.terminalBrowser.append(date + '|| Working-dircetory: ' + oscwd)
            self.progressBar.setProperty("value", 50)

            def bar_custom(current, total, width=80):
                print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
            repourl = 'https://blackzspace.org/repo/Windows/requirements.txt'
            write_file = 'requirements.txt'

            wget.download(repourl, write_file, bar=bar_custom)
            if os.path.isfile('requirements.txt'):
                print('|| requirements.txt exist!  ')
                self.terminalBrowser.append('|| requirements.txt exist! ')
                self.progressBar.setProperty("value", 70)
            else:
                print('|| requirements.txt dosent exist!!')
                self.terminalBrowser.append('|| requirements.txt dosent exist!')
                self.progressBar.setProperty("value", 0)
            self.terminalBrowser.append("|| Note: This application is using your Unix-Subsystem.")
            self.terminalBrowser.append("|| Installing and Updating dependencies.")
            stdoutdata2 = subprocess.getoutput("wsl --install")
            self.terminalBrowser.append(stdoutdata2)
            self.progressBar.setProperty("value", 75)
            stdoutdata3 = subprocess.getoutput("wsl --update")
            self.terminalBrowser.append(stdoutdata3)
            self.progressBar.setProperty("value", 80)
            print("|| Your app is now configured for Windows. Starting main.")
            self.terminalBrowser.append("|| Your app is now configured for Windows. Starting main.")
            self.progressBar.setProperty("value", 100)

        elif plat == "Linux":

            def bar_custom(current, total, width=80):
                print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

            repourl = 'https://blackzspace.org/repo/Linux/requirements.txt'
            write_file = 'requirements.txt'
            wget.download(repourl, write_file, bar=bar_custom)
            if os.path.isfile('requirements.txt'):
                print('|| requirements.txt exist!  ')
                self.terminalBrowser.append('|| requirements.txt exist! ')
                os.system("python3 -m pip install -r requirements.txt")
            else:
                print('|| requirements.txt dosent exist!!')
                self.terminalBrowser.append('|| requirements.txt dosent exist!')

            dist = subprocess.run(['grep','^NAME','/etc/os-release'], stdout=subprocess.PIPE, encoding='utf-8')
            dist.stdout
            print(dist.stdout)
            self.terminalBrowser.append(dist.stdout)

            def ubuntu(self):
                print("Your os is: Ubuntu! ")
                self.terminalBrowser.append("Your os is: Ubuntu! ")
                def bar_custom(current, total, width=80):
                    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                    self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

                repo2 = 'https://blackzspace.org/repo/Linux/ubuntu.sh'
                write = 'ubuntu.sh'
                wget.download(repo2, write, bar=bar_custom)
                if os.path.isfile('ubuntu.sh'):
                    print('|| ubuntu.sh exist!  ')
                    self.terminalBrowser.append('|| ubuntu.sh exist! ')
                else:
                    print('|| ubuntu.sh dosent exist!!')
                    self.terminalBrowser.append('|| ubuntu.sh dosent exist!')
                    os.system("sed -i 's/\r$//' ubuntu.sh")
                    os.system("chmod 777 ubuntu.sh")
                    run = 'sudo bash ubuntu.sh'  #-; ?
                    os.system(run)

            def arch(self):
                print("Your os is: Arch! ")

                self.terminalBrowser.append("Your os is: Arch! ")
                def bar_custom(current, total, width=80):
                    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                    self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                repo2 = 'https://blackzspace.org/repo/Linux/arch.sh'
                write = 'arch.sh'
                wget.download(repo2, write, bar=bar_custom)
                if os.path.isfile('arch.sh'):
                    print('|| arch.sh exist!  ')
                    self.terminalBrowser.append('|| arch.sh exist! ')
                else:
                    print('|| arch.sh dosent exist!!')
                    self.terminalBrowser.append('|| arch.sh dosent exist!')

                os.system("sed -i 's/\r$//' arch.sh")
                os.system("chmod 777 arch.sh")
                run = "sudo bash arch.sh"
                os.system(run)


            def debian(self):
                print("Your os is: Debian! ")
                self.terminalBrowser.append("Your os is: Debian! ")
                def bar_custom(current, total, width=80):
                    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                    self.terminalBrowser.append("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
                repo2 = 'https://blackzspace.org/repo/Linux/debian.sh'
                write = 'debian.sh'
                wget.download(repo2, write, bar=bar_custom)
                if os.path.isfile('debian.sh'):
                    print('|| debian.sh exist!  ')
                    self.terminalBrowser.append('|| debian.sh exist! ')
                else:
                    print('|| debian.sh dosent exist!!')
                    self.terminalBrowser.append('|| debian.sh dosent exist!')
                os.system("sed -i 's/\r$//' debian.sh")
                reply = input("NOTE: sudo installed?(Yy/Nn)")
                if reply == 'y':
                    return True
                    if reply == 'n':
                        return False
                        while True:
                            os.system("chmod 777 debian.sh")
                            run = 'sudo bash debian.sh'  #-; ?
                            os.system(run)


            if dist.stdout == 'NAME="Ubuntu"\n':
                ubuntu(self)


            if dist.stdout == 'NAME="Arch Linux"\n':
                arch(self)


            if dist.stdout == 'NAME="Debian GNU/Linux"\n':
                debian(self)









class TerminalWindow(QtWidgets.QMainWindow, Ui_TerminalWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(TerminalWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.platf()
        self.menu2()

    def menu2(self):
        date = datetime.datetime.now()
        date = str(date)
        self.consoleLog.append("\n")
        self.consoleLog.append("♠ BigBrother || (c) by BlackLeakz ||         | v.0.1 ™")
        self.consoleLog.append("\n")
        self.consoleLog.append("\n Date: " + date)
        self.consoleLog.append("\n")
        self.consoleLog.append(" 1: netstat | 2: arp | 3: ipconfig | 4: nmap-menu     ")
        self.consoleLog.append(" 5:  | 2: arp | 3: ipconfig | 4: nmap-menu 5:| whois  ")
        self.consoleLog.append(" 6: collect all | 7: nslookup-menu   8: tracert      ")
        self.consoleLog.append(" c: clear   | m: menu |  n: NemesisLauncher | w: whois       ")
        self.consoleLog.append("\n")

        self.consoleLog.append("\n")
        self.consoleLog.append("Command@$hell:> ")

    def platf(self):
        self.progressBar.setProperty("value", 0)
        date = datetime.datetime.now()
        date = str(date)
        plat = platform.system()
        print(date + "|| Detecting OS type...")
        print(date + '|| System   :', platform.system())
        print(date + '|| Node     :', platform.node())
        print(date + '|| Release  :', platform.release())
        print(date + '|| Version  :', platform.version())
        print(date + '|| Machine  :', platform.machine())
        print(date + '|| Processor:', platform.processor())
        sys = platform.system()
        node = platform.node()
        rel = platform.release()
        ver = platform.version()
        mach = platform.machine()
        proc = platform.processor()

        self.consoleLog.append(date + '|| System   : ' + sys)
        self.consoleLog.append(date + '|| Node     : ' + node)
        self.consoleLog.append(date + '|| Release  : ' + rel)
        self.consoleLog.append(date + '|| Version  : ' + ver)
        self.consoleLog.append(date + '|| Machine  : ' + mach)
        self.consoleLog.append(date + '|| Processor: ' + proc)
        self.progressBar.setProperty("value", 30)

        if plat == "Windows":
            self.progressBar.setProperty("value", 40)
            date = datetime.datetime.now()
            date = str(date)
            print(date + "|| Configuring app for your Windows-System...|><|..|<>|..|><|.")
            self.consoleLog.append(date + "|| Configuring app for your Windows-System...|><|..|<>|..|><|.")
            oscwd = os.getcwd()

            pathx = os.path.abspath(__file__)
            print(date + '|| Scriptfile :' + pathx)
            print(date + '|| Working-dircetory: ' + oscwd)
            self.consoleLog.append(date + '|| Scriptfile: ' + pathx)
            self.consoleLog.append(date + '|| Working-dircetory: ' + oscwd)
            self.progressBar.setProperty("value", 50)

        elif plat == "Linux":
            dist = subprocess.run(['grep','^NAME','/etc/os-release'], stdout=subprocess.PIPE, encoding='utf-8')
            dist.stdout
            print(dist.stdout)
            self.consoleLog.append(dist.stdout)

            def ubuntu1(self):
                print("Your os is: Ubuntu! ")
                self.consoleLog.append("Your os is: Ubuntu! ")


            def arch1(self):
                print("Your os is: Arch! ")

                self.consoleLog.append("Your os is: Arch! ")



            def debian1(self):
                print("Your os is: Debian! ")
                self.terminalBrowser.append("Your os is: Debian! ")



            if dist.stdout == 'NAME="Ubuntu"\n':
                ubuntu1(self)


            if dist.stdout == 'NAME="Arch Linux"\n':
                arch1(self)


            if dist.stdout == 'NAME="Debian GNU/Linux"\n':
                debian1(self)


    @QtCore.pyqtSlot()
    def a(self):
        self.consoleLog_inp.setDisabled(False)
        self.progressBar.setProperty("value", 1)
        self.consoleLog.append("Enter target-ip:> ")

        ip = self.consoleLog_inp.text()
        ip = str(ip)
        self.consoleLog_inp.editingFinished()
        time.sleep(1)
        nmap1 = subprocess.check_output(["wsl","nmap -v -sn " + ip],universal_newlines=True)
        nmap1 = str(nmap1)
        print(nmap1)
        time.sleep(2.4)
        self.consoleLog.append(nmap1)
        self.progressBar.setProperty("value", 100)

    @QtCore.pyqtSlot()
    def takeinputs(self):
        name, done1 = QtWidgets.QInputDialog.getText(
             self, 'Input Dialog', 'Enter target:')

        if done1:
            self.consoleLog.append('Information stored Successfully\Target:' +str(name))
        self.pushButton.hide()
        os.system("wsl nmap -v -sn " + name)
        self.progressBar.setProperty("value", 100)
    @QtCore.pyqtSlot()

    def send(self):
        self.consoleLog.append(self.terminal_inp.text())

        if self.consoleLog_inp.text() == "c":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.clear()
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() == "t":
            self.consoleLog_inp.clear()
            while True:
                try:
                    if keyboard.is_pressed('t'):
                        print("You pressed a key!")
                        self.consoleLog.append("You pressed a key.")
                        self.consoleLog_inp.clear()
                        ip = self.consoleLog_inp()
                        ip = str(ip)
                        os.system("nmap -v -sn " + ip)
                        break
                except:
                        break


        if self.consoleLog_inp.text() == "m":
            self.progressBar.setProperty("value", 0)
            self.menu2()
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() == "1":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("\n || Runin' netstat.")
        #    netstat_out = subprocess.run(['netstat', '-at'], check=True, capture_output=True).stdout
            netstat_out = subprocess.check_output(["netstat","-at"],universal_newlines=True)

            netstat_out = str(netstat_out)
            print(netstat_out)
            self.consoleLog.append(netstat_out)
            self.progressBar.setProperty("value", 100)


        if self.consoleLog_inp.text() == "2":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("\n || Runin' arp -a.")
            arp_out = subprocess.check_output(["arp","-a"],universal_newlines=True)
            arp_out = str(arp_out)
            print(arp_out)
            self.consoleLog.append(arp_out)
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() == "3":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("\n || Runin' ipconfig /all.")
            #ipconfig_out = subprocess.check_output(["ipconfig","-all"],universal_newlines=True)
        #    ipconfig_out = str(ipconfig_out)
            #print(ipconfig_out)
            ipconfig_out = subprocess.run(['ipconfig','-all'], check=True, capture_output=True).stdout
        #    ipconfig_out = subprocess.check_output(["ipconfig","-all"],universal_newlines=True)
            ipconfig_out = str(ipconfig_out)
            print(ipconfig_out)
            #stdout = subprocess.run(['ipconfig', '-all'], check=True, capture_output=True, text=True).stdout
            #stdout = str(stdout)
            self.consoleLog.append(ipconfig_out)
            self.progressBar.setProperty("value", 100)
        if self.consoleLog_inp.text() == "6":
            self.progressBar.setProperty("value", 0)
            netstat_out2 = subprocess.check_output(["netstat","-at"],universal_newlines=True)
            netstat_out2 = str(netstat_out2)
            print(netstat_out2)
            self.consoleLog.append(netstat_out2)
            self.progressBar.setProperty("value", 33)

            arp_out2 = subprocess.check_output(["arp","-a"],universal_newlines=True)
            arp_out2 = str(arp_out2)
            print(arp_out2)
            self.consoleLog.append(arp_out2)
            self.progressBar.setProperty("value", 66)

            ipconfig_out2 = subprocess.check_output(["ipconfig","-all"],universal_newlines=True)
            ipconfig_out2 = str(ipconfig_out2)
            print(ipconfig_out2)
            self.consoleLog.append(ipconfig_out2)
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() == "8":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("\n || Runin' tracert.")
            self.consoleLog.append("\n Enter IP:")

            self.consoleLog_inp.clear()
            ip = self.terminal_inp.text()
            tracert = subprocess.run(['tracert', ip], check=True, capture_output=True).stdout
            #tracert = subprocess.check_output(["tracert ", ],universal_newlines=True)
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() =="p":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("\n || Runin'")



            tracert = str(tracert)
            print(tracert)
            self.consoleLog.append(tracert)
            self.progressBar.setProperty("value", 100)

        if self.consoleLog_inp.text() == "4":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("_____________________________________")
            self.consoleLog.append("|| NMAP WSL MENU | Version: v.1.0  ||")
            self.consoleLog.append("||---------------------------------||")
            self.consoleLog.append("|| a: -sn | b: -A -O | d: -6 -sn   ||")
            self.consoleLog.append("||_________________________________||")
            self.consoleLog.append("\n")
            self.consoleLog.append("Command@$hell:> ")
            self.consoleLog.append(self.terminal_inp.text())

        if self.consoleLog_inp.text() == "a":

            self.a()

        if self.consoleLog_inp.text() == "b":
                self.progressBar.setProperty("value", 1)
                self.takeinputs()


        if self.consoleLog_inp.text() == "d":
                self.progressBar.setProperty("value", 1)
                self.consoleLog.append("Enter target-ip:> ")
                ip = self.consoleLog_inp.text()
                ip = str(ip)
                nmap1 = subprocess.check_output(["wsl","nmap -v -6 -sn " + ip],universal_newlines=True)
                nmap1 = str(nmap1)
                print(nmap1)
                self.consoleLog.append(nmap1)
                self.progressBar.setProperty("value", 1000)

        if self.consoleLog_inp.text() == "5":
            self.progressBar.setProperty("value", 0)
            self.consoleLog.append("Enter target:> ")
            self.ip()

        #if self.consoleLog_inp.text() == "w":


    def ip(self):
        ip = self.terminal.text()
        nmap1 = subprocess.check_output(["wsl","whois " + ip],universal_newlines=True)
        nmap1 = str(nmap1)
        print(nmap1)
        self.consoleLog.append(nmap1)
        self.progressBar.setProperty("value", 100)
















def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    app2 = QtWidgets.QApplication(sys.argv)
    window2 = TerminalWindow()
    window2.show()
    app2.exec()










if __name__ == '__main__':
    main()
