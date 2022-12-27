from functools import reduce
def add_two(a,b):
    return a+b
list1=[0,1,2,3,4,5,6,7,8,9]
val=reduce(add_two,list1)
print(val)

# using lambda function:-
sum_two_numbers = lambda a,b: a+b
list2=[1,2,3,4,5]
val=reduce(sum_two_numbers,list2)
print(val)