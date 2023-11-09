name0={'wang':49,'sex':'man'}
name1={'li':24,'sex':'man'}
name2={'zhang':18,'sex':'woman'}
names=[name0,name1,name2]   #注意是字典列表
for na in names:
    print(na)

locals={'sichuan':['nanchong','deyang','chengdu'],'liaoning':['shenyang','panjing']}
print(locals['sichuan'][1])
your_name=input("please input your name")
print(f"\t{your_name}")

print("\n")
your_age=int(input("age:    "))
if your_age==18:
    print(your_age)


