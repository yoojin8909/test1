x=raw_input("Enter the number: ")
x=int(x)

try:
    x != 0
    y= 10 / (x*1.0)
    print y
except:
    print '0 is not accepted'

