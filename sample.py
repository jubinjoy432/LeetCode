import sys
randomList=['a',0,2]
for entry in randomList:
    try:
        print("The entry is",entry)
        r=1/int(entry)
        break
    except:
        print("Ooops!",sys.exc_info()[1],"occured")
        print("Next Entry.")
        print()
print("The reciprocal of",entry,"is",r)

