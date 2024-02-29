#Author's names are Therese Burns and Allison Macrowski
#part A
x=2
if x<3:
    print("Small")
x=5
if x<3:
    print("Small")
score=8 #A score on a 10 point quiz
if score>6:
    print("Nice work!")
for i in range(1,16):
    if i%3==0:
        print(i, "is divisible by 3.")
number=int(input("what is your number?\n"))
if number%2==0:
    print("Even")

#part B
x=2
if x<3:
    print("Small")
else:
    print("Large")
x=5
if x<3:
    print("Small")
else:
    print("Large")
score=8
if score<6:
    print("Needs improvement")
elif score<9:
    print("Nice work!")
else:
    print("Excellent!")
for i in range(-2,3):
    if i<0:
        print(i, "is negative.")
    elif i==0:
        print(i, "is zero.")
    else:
        print(i, "is positive.")
n=int(input("Number:\n"))
if n%2==0:
    print("Even")
else:
    print("Odd")

#part C
print(3<4)
print(4>2)
type(True)
if True:
    print("This text will always appear.")
if False:
    print("This text will never appear.")
type(False)
print(3==5)
def true_false():
    x=int(input("number:\n"))
    if x>10:
        print("True")
    else:
        print("False")
true_false()       
    
    
