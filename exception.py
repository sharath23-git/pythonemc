'''try:
    a=int(input())
    b=int(input())
    print(a+b)
except Exception as e:
    print("Invalid", e)'''

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=input("Enter: ")
    #print(c/a)
    #print(d)
except ValueError as e:  #only work on value error
    print("Invalid", e)
except TypeError as e:    #only work on type error
    print("Type Error",e)
except Exception:         #work on all errors
    print("Somthing wrong")
finally:                   #finally block will execute even if there is an error
    print("Done")