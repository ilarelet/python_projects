#Exercise 1
def paycalc(t,w):
    if t>40:
        return (t-40)*1.5*w + 40*w
    else:
        return t*w

prompt="How many hours did you work?"
try:
    time = float(input(prompt))
except:
    print("Please enter a number")

prompt="What's your wage per hour?"
try:
    wage = float(input(prompt))
except:
    print("Please enter a number")

if time>0 and wage>0:
    pay = round(paycalc(time,wage),2)
else:
    print("Invalid input data")
    quit()

print("Your pay is $" + str(pay))
####################################################################################
#Exercise 2
def grade(x):
    if x>=0.9:
        return("A")
    elif x>=0.8:
        return("B")
    elif x>=0.7:
        return("C")
    elif x>=0.6:
        return("D")
    else:
        return('F')

prompt = "Enter your score: "
try:
    score = float(input(prompt))
except:
    print("Invalid score")
    quit()

if 1>=score>=0 :
    print("Your grade is " + grade(score))
else:
    print("Score is out of range")
######################################################################################
#Exercise3
i=0
sum=0
maxi = None
mini = None
while 1==1:
    cur = input("Enter your next number or type ""done"" to finish: ")
    if cur == ("done" or "Done"):
        break
    else:
        try:
            sum += float(cur)
            i += 1
            if maxi == None or maxi < float(cur):
                maxi = float(cur)
            if mini == None or mini > float(cur):
                mini = float(cur)
        except:
            print("Enter a number!")
print(str(i) + " numbers were given.")
print("The total is " +str(sum) +".")
try:
    print("The average is " +str(round(sum/i,3)) +".")
    print("The maximum is " +str(maxi) +".")
    print("The minimum is " +str(mini) +".")
except:
    print("No way to calculate average. Probably no numbers were given.")
