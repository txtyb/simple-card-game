a=['1','2','3','4','5']
b=list()

for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)
print('---------------')

try:
    p=a.index(input('输入要查找的值：'))
except ValueError:
    print('没有找到')
else:
    print('位于%s'%p)
print('--------------')

print('a= ',a)
print(a[:3])

xx=('%s'%x)
