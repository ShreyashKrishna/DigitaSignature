import sys
import hashlib
import math
import random
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
sha1 = hashlib.sha1()
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

inputfile=input("Enter the name of file to be verified:")
with open(inputfile, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)
temp=int(sha1.hexdigest(),16);
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
print("gis ",g)
print("his ",h)
f2=open("OutputSign.txt","r")
st5=f2.readline()
c1=int(st5)
st6=f2.readline()
c2=int(st6)
f2.close();
invc2=Extended(c2,q);#here we get inverse
t1=(temp*invc2)%q;
print(c1);
t2=(c1*invc2)%q;
g1=SquareAndMultiply(g,t1,p);
g2=SquareAndMultiply(h,t2,p);
check=((g1*g2)%p)%q;
print(check)
if(check==c1):
    print("Valid Signature");
else:
    print("Invalid Signature");
