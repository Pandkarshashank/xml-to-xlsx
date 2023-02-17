import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('Input.xml')
root = tree.getroot()
file = open('XML3.txt','w')
file.truncate()
importdata = root[1][0]
tallymessage = importdata[1][1]
voucher = tallymessage[0]

tallyArray = []
voucherArray = []

for tallymessage in importdata:
    for voucher in tallymessage:
        tallyArray.append(voucher)
        for v in voucher:
            voucherArray.append(v)
        tallyArray.append(voucherArray)

transactionType=[]

for voucherArray in tallyArray:
    vouchers=[]
    for voucher in voucherArray:
        dict={}
        for data in voucher:
            dict.update({data.tag:data.text})
        vouchers.append(dict)


