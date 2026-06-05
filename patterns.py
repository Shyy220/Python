for i in range(4):
    print("* * * *")



for i in range(1,6):
    print("*" *i)


for i in range(1,6):
    print(i*str(i))


i = 1
while i<=5:
    print("*" *i)
    i+=1


for i in range(4):
    for j in range(4):
        print("*",end = " ") 
    print()


for i in range(1,6):
    for j in range(i):
        print("*",end = " ")
    print()


for i in range(1,6):
    for j in range(i):
        print(i, end = " ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()



for i in range(5,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
    