import hashlib # for SHA256 computation
import binascii # for conversion between Hexa and bytes

entropy = "c10ec20dc3cd9f652c7fac2f1230f7a3c828389a14392f05" 

data = entropy.strip() #cleaning of data
data = binascii.unhexlify(data)
if len(data) not in [16, 20, 24, 28, 32]:
   raise ValueError(
  "Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (%d)." % len(data)
   )
   
h = hashlib.sha256(data).hexdigest()
b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]

with open("wordlist/english.txt", "r") as f:
    wordlist = [w.strip() for w in f.readlines()]

seed = []
for i in range(len(b)//11):
    indx = int(b[11*i:11*(i+1)],2)
    seed.append(wordlist[indx])

print(seed) 

    