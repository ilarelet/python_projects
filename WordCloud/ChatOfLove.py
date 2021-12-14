ignore = ["Lillie \n", "L \n", "Ilyushka \n", "I \n", "file:///C", "Exported Data \n"]
ign_punct = ")(*?&.,!^/;:\"‘“”☺#"
stopwords = open("WordCloud/stopwords")
prompt="Please enter filename:"
try:
    file = open(prompt)
except:
    print("File ",prompt,' not found:(')
newfile = open("newfile.txt", "w")

ign_words=[]
for line in stopwords:
    ign_words.append(line[:-1])
stat=dict()

for line in file:
    if not any(ign_line in line for ign_line in ignore):
        newfile.write(line)

newfile = open("newfile.txt", "r")
for line in newfile:

    words=line.split()

    for word in words:
        for sym in word:
            if sym in ign_punct:
                word=word.replace(sym,'')
            if sym == "'":
                word=word.replace(sym,'\\\'')
        word=word.lower()

        if word not in stat:
            stat[word]=1
        else:
            stat[word]+=1

wds = list()

for word, val in stat.items():
    if word != "" and word[0] not in "0123456789" and word[:4] != "http":
        if word not in ign_words:
            wds.append((val, word))   

wds.sort(reverse=True)


maxx = None
minn = None

for val, word in wds[:100]:
    if maxx == None or val > maxx:
        maxx = val
    if minn == None or val < minn:
        minn = val
print("The range is from ",maxx, " to ",minn )

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('WordCloud/gword.js','w')
fhand.write("gword = [")
first = True
for val, word in wds[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = (val - minn) / float(maxx - minn)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+word+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()
file.close()
newfile.close()
