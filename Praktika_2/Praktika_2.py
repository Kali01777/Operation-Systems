import hashlib
from threading import Thread

hs1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
hs2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
hs3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
slovar = []#26
ot1, ot2, ot3 = "", "", ""
for i in range(97, 123):
    slovar.append(chr(i))
while True:
    v = int(input("Введите кол-во потоков (1-4) : "))
    if 0<v<5 or v==8:
        break
    print("Введено неверное значение!")
def zero(x, l):
    for a1 in slovar[x:l]:
        for a2 in slovar[x:26]:
            for a3 in slovar[x:26]:
                for a4 in slovar[x:26]:
                    for a5  in slovar[x:26]:
                        slovo = a1+a2+a3+a4+a5
                        hash_object = hashlib.sha256(bytes(slovo, encoding = "utf-8"))
                        hex_dig = hash_object.hexdigest()
                        if hex_dig == hs1:
                            s1=hs1 + " = " + slovo
                            print(s1)
                        if hex_dig == hs2:
                            s2 = hs2 + " = " + slovo
                            print(s2)
                        if hex_dig == hs3:
                            s3 = hs1 + " = " + slovo
                            print(s3)


if v == 1:
    zero(0, 26)
if v == 2:
    thread_1 = Thread(target=zero, args=(0,13))
    thread_2 = Thread(target=zero, args=(13, 26))
    thread_1.start()
    thread_2.start()
if v == 3:
    thread_1 = Thread(target=zero, args=(0,9))
    thread_2 = Thread(target=zero, args=(9,18))
    thread_3 = Thread(target=zero, args=(18,26))
    thread_1.start()
    thread_2.start()
    thread_3.start()
if v == 4:
    thread_1 = Thread(target=zero, args=(0, 7))
    thread_2 = Thread(target=zero, args=(7, 14))
    thread_3 = Thread(target=zero, args=(14, 20))
    thread_4 = Thread(target=zero, args=(20, 26))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

