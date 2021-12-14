degfile=open('degrees.py','r')
#hugestr=degfile.read()
#print('There are '+str(len(hugestr))+' characters.')

i=0
for line in degfile:
    if 'print' in line:
        i+=1
        line=line.rstrip()
        print(str(i)+": "+line)
print('There are '+str(i)+' prints in the file.')