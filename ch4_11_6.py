names=['wang','li','zhang']
for name in names:
    print(f"{name.title()},welcome to python")
for value in range(1,5):
    print(value)
print(f"{names[0].title()},welcome again")
'''
z这里是注释格式
'''
values=list(range(1,11,2))  #这里也是注释  从1到11，以2递增转为列表
print(values)


nums=[]
for num in range(1,11,2):
    nums.append(num**2)   #这里**符号是平方的意思
print(nums)
print(f"nums[0]={nums[0]}")  #  思考这句和print("nums[0]={nums[0]}")有什么区别
print(f"min={min(nums)}")   #三个常用函数
print(f"max={max(nums)}")
print(f"sum={sum(nums)}")