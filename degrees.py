def FtoC(f):
    c=(f-32)/9*5
    return c

def CtoF(c):
    f=c*9/5+32
    return f

flag=input('Type "c" if you need to convert Celsius to Fahrenheit or type "f" if you need to convert Fahrenheit to Celsius: ')
if flag=='c' or flag=='C':
    C=input('Enter your temperature in Celsius: ')
    F=CtoF(float(C))
    print('it is '+str(round(F,2))+' degrees Fahrenheit!')
elif flag=='f' or flag=='F':
    F=input('Enter your temperature in Fahrenheit: ')
    C=FtoC(float(F))
    print('it is '+str(round(C,2))+' degrees Celsius!')
else:
    print('What have you done?... it was supposed to be C or F...\nNow we need to restart the program.')