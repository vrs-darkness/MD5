from collections import defaultdict as dd
from math import *

global r  # left Shift Constant
r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17,22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9,\
      14,20, 5, 9, 14, 20, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11,16, 23, 4, 11, 16, 23, 6, 10, 15,\
          21, 6, 10, 15, 21, 6,10, 15, 21, 6, 10, 15, 21] 
global k # iteration Constant
k = [floor(abs(sin(i))*(2**32)) for i in range(0,64)]


def Stringtobinary(Msg):
                                                                         # Converting the given string into Binary Number
    Input = ""
    for i in Msg.split():
        for j in i :
            Input += bin(ord(j))[2:]
    return Input

def Paddingtobit(Input):
                                                                # using this function we would be converting the msg into requirements(Must be in multiples of 512-bits )
    temp = Input
    length = len(temp)
    if(len(temp)%512!=0):
        # Padding bit insertion starts
        temp += '1' 
        n = ceil(len(temp)/512)
        # print(n)
        # print(len(temp))
        if(abs(len(temp)-512)<64 or abs((512*n)-len(temp))<64 ):
            if(n==0):
                temp += ("0"*abs(((512)) - len(temp)))
            else:
                temp += "0" * abs( len(temp) - ((n*512)) )
        else:
            if(n==0):
                temp+=("0"*abs(((512)-64) - len(temp)))
            else:
                temp += "0" * abs( len(temp) - ((n*512)-64) )
            # Padding Bit insertion stops
            additional = bin(length)[2:]
            if(len(additional)>64):
                additional = bin(int(additional,2) % (2**64))[2:]
            temp+= "0"*(64 - len(additional))
            temp += additional # Length Bit
    return temp

def Splitter(Msg,n):
                                                                # This Function helps us to split the processed message into n parts
    if(len(Msg)==n):
        temp = [Msg]
    else:
        temp = [Msg[i:i+n] for i in range(0,len(Msg),n)]
    return temp 

def Encrypt(Msg,A,B,C,D):
    Q = dd()
    Q[-4],Q[-3],Q[-2],Q[-1] = A,B,C,D                   # Intialized the Chain Variables
    for step in range(0,64):
        if (step>=0 and step <=15):         # Round 1 (16 times execution of Function F)
            phi = hex((int(Q[step-1],16) & int(Q[step-2],16)) | (~(int(Q[step-2],16)) & int(Q[step-3],16)))[2:]
            g = step
        elif(step>=16 and step<=31):        # Round 2 (16 times execution of Function G)
            phi = hex((int(Q[step-1],16) & int(Q[step-2],16)) | (~(int(Q[step-2],16)) & int(Q[step-3],16)))[2:]
            g = (5*step  + 1 ) % 16
        elif (step>=32 and step<=47):       # Round 3 ( 16 times execution of Function H)
            phi = hex((int(Q[step-1],16) ^ int(Q[step-2],16) ^ int(Q[step-3],16)))[2:]
            g = (5*step  + 1 ) % 16
        elif (step>=48 and step<=63):      # Round 4 ( 16 times execution of Function I)
            phi = hex((int(Q[step-2],16)) ^ (int(Q[step-1],16) | ~(int(Q[step-3],16))))
            phi = phi[phi.index('x')+1 : ]
            g = (7*step + 1 ) % 16
        else:
            pass
        # Below step we will be changing D variable of the current iteration using the below step
        Q[step] = hex(((((((((int(phi,16) + int(Q[step-4],16)) % (2**32)) + k[step]) %(2**32)) + int(Msg[g],2))%(2**32)) << r[step] ) + int(Q[step-1],16) )%(2**32))[2:]
    # Updation step
    A,B,C,D = Q[60],Q[61],Q[62],Q[63]
    return A,B,C,D



def Main1(Msg):
        # Intializing MD Buffers
    A = hex(int("67452301",16))[2:]
    B = hex(int("efcdab89",16))[2:]
    C = hex(int("98badcfe",16))[2:] 
    D = hex(int("10325476",16))[2:]
    I1 = Splitter(Paddingtobit(Stringtobinary(Msg)),512)
    for i_msg in I1 : # For every 512-Bit Block 
        # s  = Splitter(i_msg,32)
        # print(*[len(i) for i in s])
        A,B,C,D = Encrypt(Splitter(i_msg,32),A,B,C,D)
    Hash = A+B+C+D
    Hash = "0"*(32-len(Hash)) + Hash    
    return Hash

def Key_based_md5(Msg,key ="790abe22",salt ="89eea11"):
    # Chaining method and XOR(Exclusive OR) cipher
    A = hex(int("67452301",16))[2:]
    B = hex(int("efcdab89",16))[2:]
    C = hex(int("98badcfe",16))[2:] 
    D = hex(int("10325476",16))[2:]

    I1 = Splitter(Paddingtobit(Stringtobinary(Msg+salt+key)),512)
    for _ in range(100):
        for i_msg in I1 : # For every 512-Bit Block 
            A,B,C,D = Encrypt(Splitter(i_msg,32),A,B,C,D)

        Hash = A+B+C+D
    return Hash

if __name__=='__main__':
    Msg = input("Enter the Message : ")
    Hash1 = Main1(Msg)
    print("Hash Output (Simple MD5): " , Hash1)
    Hash2 = Key_based_md5(Msg)
    print("Hash Output(strengthened MD5):",Hash2)




