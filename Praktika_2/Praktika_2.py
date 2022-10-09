import hashlib

hs1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
hs2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
hs3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
slovar = []
for i in range(97, 123):
    slovar.append(chr(i))
for a1 in slovar:
    for a2 in slovar:
        for a3 in slovar:
            for a4 in slovar:
                for a5  in slovar:
                    slovo = a1+a2+a3+a4+a5
                    hash_object = hashlib.sha256(bytes(slovo, encoding = "utf-8"))
                    hex_dig = hash_object.hexdigest()
                    if hex_dig == hs1:
                        ot1 = slovo
                    if hex_dig == hs2:
                        ot2 = slovo
                    if hex_dig == hs3:
                        ot3 = slovo

print(ot1, "=", hs1)
print(ot2, "=", hs2)
print(ot3, "=", hs3)
