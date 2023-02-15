import xmlparser as xp

file=open('XML.txt')

lines=file.readlines()

print(lines[:20])

for i in range(20):
    if(lines[i]=='  VOUCHER : \n'):
        print(lines[i])
