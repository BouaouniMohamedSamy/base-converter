print("Welcome to the base converter!")
print("Please enter your number in decimal form :")
n = int(input())
print("Now enter in which base you want to convert your number <= 10 :")
x = int(input())
while x <=0 or x > 10:
    print("Enter a number between 2 and 10 please : ")
    x = int(input())
def decimal_base(a,base):
    b = 0
    i = 1
    if base == 1 :
       b = 1
       for p in range(a-1):
           p = 1
           b = (str(p) + str(b))
    else:
       while a > 0:
          r = a % base
          b = b + r*i
          a = int(a / base)
          i = i*10
    if a == 10:
        b = a
    return b
    print("your number in base of  " + str(x) + " is:" + str(decimal_base(n,x)))








