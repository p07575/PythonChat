#導庫
import socket
import random
import os
import keyboard
import sys
import time
#from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back, Style

#定義變量
cons = "0"

#定義連接服務器類
class connServer:
    def __init__(self):
        self.cs = False

#面向對象（服務器類）
sc = connServer()

def sysexit():
    os.system("cls")
    print("感謝使用簡易通訊！")
    print("Bye!")
    exit = os._exit(os.X_OK)
    return exit

#定義主菜單功能
def menu():
    os.system("cls")
    print("----------------------------------------------------------------")
    if sc.cs == False:
        print("| 服務器連接狀態： "+ Fore.RED + "未連接" + Fore.RESET +"   簡易通訊              作者：項敬軒 |")
    elif sc.cs == True:
        print("| 服務器連接狀態： "+ Fore.GREEN + "已連接" + Fore.RESET +"   簡易通訊              作者：項敬軒 |")
    print("|                                                              |")
    print("| 功能：                                                       |")
    print("|                                                              |")
    print("|1) 連接服務器                                                 |")
    print("|                                                              |")
    print("|2) 創建群聊                                                   |")
    print("|                                                              |")
    print("|3) 加入群聊                                                   |")
    print("|                                                              |")
    print("|4) 退出軟件                                                   |")
    print("----------------------------------------------------------------")
    if __name__ == '__main__':
        keyboard.add_hotkey('1', ConnectServer)
        keyboard.add_hotkey('2', createGroup)
        #keyboard.add_hotkey('3', cleardic)
        keyboard.add_hotkey('4', sysexit)
        keyboard.add_hotkey('esc', menu)
        keyboard.add_hotkey('ctrl+c', sysexit)
        keyboard.wait('ctrl+c')

#定義主菜單（無鍵盤識別功能）功能
def mprint():
    os.system("cls")
    print("----------------------------------------------------------------")
    if sc.cs == False:
        print("| 服務器連接狀態： "+ Fore.RED + "未連接" + Fore.RESET +"   簡易通訊              作者：項敬軒 |")
    elif sc.cs == True:
        print("| 服務器連接狀態： "+ Fore.GREEN + "已連接" + Fore.RESET +"   簡易通訊              作者：項敬軒 |")
    print("|                                                              |")
    print("| 功能：                                                       |")
    print("|                                                              |")
    print("|1) 連接服務器                                                 |")
    print("|                                                              |")
    print("|2) 創建群聊                                                   |")
    print("|                                                              |")
    print("|3) 加入群聊                                                   |")
    print("|                                                              |")
    print("|4) 退出軟件                                                   |")
    print("----------------------------------------------------------------")

def ConnectServer():
    while True:
        SERVER_HOST = input("請輸入服務器域名或IP地址進行連接>>> ")
        while True:
            try:
                SERVER_PORT = int(input("Port>>>")) # server's port
                break
            except:
                print("這不是一個有效的端口，請重新輸入！")

        # initialize TCP socket
        s = socket.socket()
        # connect to the server
        print(f"[*] 服務器正在連接 {SERVER_HOST}:{SERVER_PORT}...")
        while True:
            try:
                s.connect((SERVER_HOST, SERVER_PORT))
                sc.cs = True
                break
            except:
                print("服務器連接失敗！"+"\n"+"請檢查您剛才所輸入的服務器資料並重新輸入。"+"\n"+"如果還是不能登入服務器，請聯繫作者本人解決問題。"+"\n"+"郵件地址：jason666nbb@gmail.com")
                break
        if sc.cs == True:
            break

    print("[+] 服務器連接成功.")
    mprint()

def createGroup():
    os.system("cls")
    if sc.cs != True:
        print("您目前還未加入服務器！"+"\n"+"請加入服務器後再創建群聊！")
        time.sleep(1.14514)
        mprint()
    elif sc.cs == True:
        print("此功能尚未完善，大約會在一星期內完善。"+"\n"+"請在大約一星期後在官網重新下載！"+"\n"+"感謝支持！")

menu()
os.system("pause")
