from collections import defaultdict as dd
from math import floor, sin, ceil


class MD5():
    def __init__(self, key=None, salt=None):

        # These values for r and k are picked from the documentations

        # Intializing MD Buffers
        self.A = hex(int("67452301", 16))[2:]
        self.B = hex(int("efcdab89", 16))[2:]
        self.C = hex(int("98badcfe", 16))[2:]
        self.D = hex(int("10325476", 16))[2:]

        self.r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4,
                  11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6,
                  10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

        self.k = []

        for i in range(0, 64):
            self.k.append(floor(abs(sin(i))*(2**32)))

    def _Stringtobinary(self, Msg: str) -> str:
        # Converting the given string into Binary Number
        binary_string = ""
        for i in Msg.split():
            for j in i:
                binary_string += bin(ord(j))[2:]
        return binary_string

    def _Paddingtobit(self, Input: str) -> str:
        # using this function we would be converting the msg into requirements\
        # (Must be in multiples of 512-bits )
        temp = Input
        length = len(temp)
        if (len(temp) % 512 != 0):
            # Padding bit insertion starts
            temp += '1'
            n = ceil(len(temp)/512)
            # print(n)
            # print(len(temp))
            if (abs(len(temp)-512) < 64 or abs((512*n)-len(temp)) < 64):
                if (n == 0):
                    temp += ("0"*abs(((512)) - len(temp)))
                else:
                    temp += "0" * abs(len(temp) - ((n*512)))
            else:
                if (n == 0):
                    temp += ("0"*abs(((512)-64) - len(temp)))
                else:
                    temp += "0" * abs(len(temp) - ((n*512)-64))
                # Padding Bit insertion stops
                additional = bin(length)[2:]
                if (len(additional) > 64):
                    additional = bin(int(additional, 2) % (2**64))[2:]
                temp += "0"*(64 - len(additional))
                temp += additional  # Length Bit
        return temp

    def _Splitter(self, Msg: str, n: int) -> str:
        # This Function helps us to split the processed message into n parts
        if (len(Msg) == n):
            temp = [Msg]
        else:
            temp = [Msg[i:i+n] for i in range(0, len(Msg), n)]
        return temp

    def _Encrypt(self, Msg: str):
        Q = dd()
        # Intialized the Chain Variables
        Q[-4], Q[-3], Q[-2], Q[-1] = self.A, self.B, self.C, self.D
        for step in range(0, 64):
            if (step >= 0 and step <= 15):
                # Round 1 (16 times execution of Function F)
                phi = hex((int(Q[step-1], 16) & int(Q[step-2], 16)) | (~(
                    int(Q[step-2], 16)) & int(Q[step-3], 16)))[2:]
                g = step
            elif (step >= 16 and step <= 31):
                # Round 2 (16 times execution of Function G)
                phi = hex((int(Q[step-1], 16) & int(Q[step-2], 16)) | (~(int(
                    Q[step-2], 16)) & int(Q[step-3], 16)))[2:]
                g = (5 * step + 1) % 16
            elif (step >= 32 and step <= 47):
                # Round 3 ( 16 times execution of Function H)
                phi = hex((int(Q[step-1], 16) ^ int(Q[step-2], 16) ^ int(
                    Q[step-3], 16)))[2:]
                g = (5 * step + 1) % 16
            elif (step >= 48 and step <= 63):
                # Round 4 ( 16 times execution of Function I)
                phi = hex((int(Q[step-2], 16)) ^ (int(Q[step-1], 16) | ~(
                    int(Q[step-3], 16))))
                phi = phi[phi.index('x')+1:]
                g = (7 * step + 1) % 16
            else:
                pass
            # Below step we will be changing D variable of the current\
            # iteration using the below step
            Q[step] = hex(((((((((int(phi, 16) + int(Q[step-4], 16)) % (
                2**32)) + self.k[step]) % (2**32)) + int(Msg[g], 2)) % (
                    2**32)) << self.r[step]) + int(Q[step-1], 16)) % (
                        2**32))[2:]
        # Updation step
        self.A, self.B, self.C, self.D = Q[60], Q[61], Q[62], Q[63]

    def Encrypt_MD5(self, Msg):
        I1 = self._Splitter(self._Paddingtobit(self._Stringtobinary(Msg)), 512)
        for i_msg in I1:
            # For every 512-Bit Block
            # s  = Splitter(i_msg,32)
            # print(*[len(i) for i in s])
            self._Encrypt(self._Splitter(i_msg, 32))
        Hash = self.A+self.B+self.C+self.D
        Hash = "0"*(32-len(Hash)) + Hash
        return Hash

    def Encrypt_Salted_MD5(self, Msg, key="790abe22", salt="89eea11"):
        I1 = self._Splitter(self._Paddingtobit(self._Stringtobinary(
            Msg+salt+key)), 512)
        for _ in range(100):
            for i_msg in I1:
                # For every 512-Bit Block
                self._Encrypt(self._Splitter(i_msg, 32))

            Hash = self.A + self.B + self.C + self.D
        return Hash
