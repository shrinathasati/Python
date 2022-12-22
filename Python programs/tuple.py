t=(0,1,2,3,4,5)
print(t)
print(type(t))
print(t[0])
print(t[-1])
print(t.count(0))
print(t.index(5))

## Empty tuple.
t1=()
print(type(t1))
print(t1)
## tuple with single value.
t2=(1)#not a valid way because this will be int class type.
print(type(t2))
print(t2)
t3=(2,)#it is a valid way to create a tuple with single value.
print(type(t3))
print(t3)