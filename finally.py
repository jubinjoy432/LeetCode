try:
    print(x)#type:ignore
except:
    print("Something went wrong!")
finally:
    print("The try except is finished")