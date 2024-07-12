import csv
import MD5
from tqdm import tqdm

files = ['CODE/List of passwords/password1.txt','CODE/List of passwords/pasword2.txt','CODE/List of passwords/password3.txt']

Pass = []

for j in files:
    f = open(j,"r")
    s = f.readlines()
    for i in range(2,len(s),4):
        pos1 = s[i].index('>')
        pos2 = s[i].index('</td>')
        temp  = s[i] [pos1+1:pos2-1]
        if (temp not in Pass):
            Pass.append(s[i][pos1+1:pos2-1])
    f.close()

D = open("Password_register.csv","w")

CSVR = csv.writer(D)
Hash = []
for i in Pass:
    Hash.append(MD5.Main1(i))

CSVR.writerow(['Password','Hash'])
for i in tqdm(range(0,len(Pass))):
    CSVR.writerow([Pass[i],Hash[i]])

D.close()
