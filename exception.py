try:
    num=int(input("Enter a number:"))
    assert num % 2 == 0
except:
    print("Not an even Number!")
else:
    reciprocal = 1/num
    print(reciprocal)

