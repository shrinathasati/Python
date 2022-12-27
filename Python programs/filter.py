greater_than= lambda num : num>5
list1=[1,8,7,6,2,789,45,5,55,4564]
print(list1)
print("elements which are greater than 5: ",list(filter(greater_than,list1)))