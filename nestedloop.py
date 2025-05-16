f'''or i in range (1,3):
    print("week: ",i)
    for j in range(1,4):
        print("\tday:",j)'''

#Example 1 star

''''for i in range(1,6):
    print()
    for j in range(i):
        print("*",end="")'''

#Example 2 pyramid

'''for i in range(1,6):
    print()
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")'''

for i in range(1,6):
    print(" "* (5-i)+"*"*(2*i-1))
