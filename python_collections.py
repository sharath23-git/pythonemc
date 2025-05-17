''' Python Collections  ////////////////////////////////////////////////////////
1.List[]'''


#Example 1 insert in list using append() and insert()

'''a=[1,2,3,4,5,"aaa","sss","bbb"]
print(a)
a.insert(1,"box")
a.append(45)
print(a)'''

#Example 2 modify the lish

'''a=[1,2,3,4,5,6]
print(a)
a[0]=11  #inserting 11 in the place of 1
a[1:3]=[22,33]  #inserting 22 and 33 in the place of 2 and 3
print(a)'''

# Example to remove from list using pop() and remove()

'''a=[1,2,3,4,5,6]
print(a)
a.pop(1)  # to remove the element in the index
a.remove(3)  #to remove the exact element using the element name
print(a)'''

#Example to merge the list using extend()

'''a=[1,2,3,4]
b=[4,5,6,7]
a.extend(b)
print(a)'''

'''Python collections /////////////////////////////////////////////////////////
2. Tuple()'''

'''a=(1,2,3,4,5)
print(a)'''

#Example casting tuple to list
'''a=(1,2,3,4,5)
b=list(a)
print(a)
print(b)
#a.append(6) # we cannot add any element to tuple'''

''' Python collections /////////////////////////////////////////////////////////
3. Set{}'''

#Example to create a set

'''a={7,1,2,3,4}
print(a)
a.add(5)
print(a)
a.remove(2)
print(a)
a.pop()
print(a)'''

'''python collections /////////////////////////////////////////////////////////
4. Dictionary{}'''

'''a={
    "name":"sai",
    "age":22,
    "place":"hyd",
    "student":"[sai,ram,krishna]"
}
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a["name"])'''


'''a={
    "name":"sai",
    "age":22,
    "place":"hyd",
    "student":"[sai,ram,krishna]"
}
a["age"]=25 #modifying the value of age
a["colour"]="red" #adding new key and value
print(a)
del a["name"]
print(a)
a.pop("age") #removing the key and value
print(a)
a.clear() #clearing the dictionary
print(a)'''

