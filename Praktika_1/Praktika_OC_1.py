import json
import os
import zipfile
import psutil
import xml.etree.ElementTree as ET


k = True
while k:
    zad = input("Введите задание (Или напишите 'ex' для выхода) : ")
    if zad == "ex":
        break;
    elif zad == "1":
        r = psutil.disk_partitions()
        print(r)


    elif zad == "2":
        z = input("Введите что вписать в файл : ")
        with open("Zadanie_2.txt", "w") as file:
            file.write(z+"\n")
        with open("Zadanie_2.txt", "r") as f:
            print(f.read())
    elif zad == "3":
        dat_0= []
        dat_1 = []
        dat_0.append(input("Введите данные через пробел для data_0 : ").split())
        dat_1.append(input("Введите данные через пробел для data_1 : ").split())
        to_json = {"data_0" : dat_0, "data_1" : dat_1}
        with open("Zadanie_3.json", "w") as f:
            json.dump(to_json, f)
        with open("Zadanie_3.json") as f:
            print(f.read())

    elif zad == "4":
        with open("Zadanie_4.xml", "r") as xm:
            print(xm.read())

    elif zad == "5":
        with open("Zadanie5.txt", "w") as f:
            f.write(input("Запишите то что хотите в файл, который перенесётся в архив : "))
        with zipfile.ZipFile("Zadanie_5.zip", "w") as f:
            f.write("Zadanie5.txt")
            m = input("Файл в архиве. Нажмите Enter для продолжения : ")
            f.extract("Zadanie5.txt")
            m = input("Файл разархивирован. Нажмите Enter для продолжения : ")
        print("Размер файла :", os.path.getsize("Zadanie5.txt"))
        os.remove("Zadanie5.txt")
        os.remove("Zadanie_5.zip")

