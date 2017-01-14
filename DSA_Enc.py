import math
import random
import hashlib
import sys
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
sha1 = hashlib.sha1()
def Extended(a,b):
    a0=a
    b0=b
    t0=0
    t1=1
    s0=1
    s=0
    q=math.floor(a0/b0)
    r=a0-q*b0
    while(r>0):
        temp=t0-(q*t1)
        t0=t1
        t1=temp
        temp=s0-(q*s)
        s0=s
        s=temp
        a0=b0
        b0=r
        q=math.floor(a0/b0)
        r=a0-(q*b0)
    r=b0;
    retval=[r,s,t1]
    return (s%b);
def SquareAndMultiply(k,c,n):
    bin_e=bin(c)[2:]
    c1=[]
    for bit in bin_e:
        c1.append(int(bit));
    c1.reverse()
    l=len(bin(c)[2:])
    z=1    
    for i in range(l-1,-1,-1):
        z=(z*z)%n
        if c1[i]==1:
            z=(z*k)%n    
    return z
f1=open("VerKey.txt","r")
st1=f1.readline()
st2=f1.readline()
st3=f1.readline()
st4=f1.readline()
f1.close()
p=int(st1)
q=int(st2)
g=int(st3)
h=int(st4)
f2=open("SignKey.txt","r")
st5=f2.readline()
f2.close()
a=int(st5)
inputfile=input("Enter the name of the file to be signed")
with open(inputfile, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
temp=int(sha1.hexdigest(),16)#the integer version here
flag=True
while(flag):
    flag=False
    r=random.randint(1,q-1);#a random numbert is generated
    c1a=SquareAndMultiply(g,r,p);#c1a is created
    c1=c1a%q;# c1 is produced
    #openedFile = open(inputFile, 'rb')#so here the inputfile is opened
    inver=Extended(r,q);#inverse of r
    print("r is",r);
    print("q",q);
    c2=((temp+a*c1)*inver)%q;
    print(c1)
    print(c2)
    if(c1==0 or c2==0):
        flag=True

fo = open("OutputSign.txt", "a")
fo.write(str(c1))
fo.write("\n")
fo.write(str(c2))
fo.write("\n")
fo.close();
