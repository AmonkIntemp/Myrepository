'''
names=['wang','li','zhang','huan']
print(names[0:2])    #列表切片
print(names[:])
names_copy1=names[:]   #复制列表
names_copy1.append('tang')
print(names)
print(names_copy1)
names_copy2=names   #这只是指向names对象，指向的是同一个存储地址
names_copy2.append('shang')
print(names)
print(names_copy2)

locals=('nanchong','chengdu','mianyang')
print(locals[:])

#locals[1]='newcity'   报错元祖的值不能被耽搁修改


'''





names=['wang','li','zhang','huan']
if 'wang' in names:
    print("wang is here")
for name in names:
    if name=='wang':
        print("wang is here")
    elif name=='li':
        print("li is here")
    else:
        print("othres")

locals={'nanchong':511304,'mianyang':511300,'chengdu':511301}
print(locals)
print(locals['nanchong'])
locals['deyang']=511302
print(locals)
del locals['mianyang']
print(locals)

print("\n")
'''
for local,value in locals.items():    #遍历键值对
    print(f"local={local}")
    print(value)

for key in locals.keys():
    print(key)
'''
for local in set(locals.values()):   #集合可以去掉重复的值
    print(local)

