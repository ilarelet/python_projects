#Exercise4

str1 = 'X-DSPAM-Confidence:0.8475'
pos = str1.find(":")
print(str(pos))
num = float(str1[pos+1:])
print(str(num))
