from my_lib_11_9 import *
names={}
active=False
while active:
    name=input("please input your name:    ")
    names[name]=int(input("please input your age:    "))
    print(names)
    if input("would you liek to repeat? :    (yes or no)")=='yes':
        active=True
    else:
        active=False
locals={'nanchong':'good','deyang':'good'}


greet(locals)



strings=['one','two','three']
strings=change_string(strings[:])
print(strings)
