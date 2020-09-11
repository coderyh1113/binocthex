import time
import os
import socket

os.system('clear')

while True:
    print("                    ----------                     ")
    print("                 -----------------                   ")
    print("              ------------------------                 ")
    print("\033[31m" + "-  Binary, octal, hexadecimal automatic conversion program  -")
    print("\033[37m" + "              ------------------------                 ")
    print("                 -----------------                   ")
    print("                    ----------                     ")
    print("               made by coder yh                 ")
    print("")
    print("[1] Binary number")
    print("[2] Octal number")
    print("[3] Hexadecimal number")
    print("[4] Object's eigenvalue (same role as Python's id())")
    print('[5] exit this program')
    a = input("choose: ")
    if a == "1":
        bina = input("integer to convert to Binary: ")
        time.sleep(0.3)
        print(bin(int(bina)))
        time.sleep(1)
        input("press enter to continue...")
        os.system('clear')
        time.sleep(0.99)
    elif a == "2":
        octa = input("integer to convert to Octal: ")
        time.sleep(0.3)
        print(oct(int(octa)))
        time.sleep(1)
        input("press enter to continue...")
        os.system('clear')
        time.sleep(0.99)
    elif a == "3":
        hexa = input("integer to convert to Hexadecimal: ")
        time.sleep(0.3)
        print(hex(int(hexa)))
        time.sleep(1)
        input("press enter to continue...")
        os.system('clear')
        time.sleep(0.99)
    elif a == "4":
        ida = input("String for which you want to know the unique value (It works like Python's id()): ")
        time.sleep(0.3)
        print(id(ida))
        time.sleep(1)
        input("press enter to continue...")
        os.system('clear')
        time.sleep(0.99)
    elif a == "5":
        print("-  bye, bye  -")
        break
    else:
        print("Something is wrong.")
        print("please try again.")
        print("")
        input("press enter to continue...")
        os.system('clear')
        time.sleep(0.99)
