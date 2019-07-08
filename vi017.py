num = int(input("Enter: "))
print (10 / num)

try:
    num = int(input("Enter: "))
    print (10/num)
except ZeroDivisionError:
    print("Can't not divide.")
except ValueError:
    print("Input must exist.")
