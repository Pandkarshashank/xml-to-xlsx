import xml.etree.ElementTree as ET

file=open('XML.txt','w')
file2=open('XML2.txt','w')
file2.truncate()
tree = ET.parse('Input.xml')
root = tree.getroot()

importdata = root[1][0]
tallymessage = importdata[1][1]
voucher = tallymessage[0]

def writefile(file,tag,text,n):
    string=''
    for i in range(n):
        string+=" "
    if(text!=None):
        file.write((string + tag + " : " +text +'\n'))
    else:
        file.write((string + tag + " : " + 'None' + '\n'))

def basefile(file,tag,text):
    if(text!=None):
        file.write((tag+":"+text +" "))
    else:
        file.write((tag +":"+ 'None'+ " "))

for tallymessage in importdata:
    writefile(file,tallymessage.tag,tallymessage.text,0)
    basefile(file2,tallymessage.tag,tallymessage.text)
    for voucher in tallymessage:
        writefile(file,voucher.tag,voucher.text,1)
        basefile(file2,voucher.tag,voucher.text)
        for x in voucher:
            writefile(file,x.tag,x.text,2)
            basefile(file2,x.tag,x.text)
            for k in x:
                writefile(file,k.tag,k.text,3)
                basefile(file2,k.tag,k.text)
                for i in k:
                    writefile(file,i.tag,i.text,4)
                    basefile(file2,i.tag,i.text)
                    for l in i:
                        writefile(file,l.tag,l.text,5)
                        basefile(file2,l.tag,l.text)
                    

