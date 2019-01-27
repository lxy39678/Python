# 1. 把1000-2500之间，既能被7整除，也能被5整除的数取出来， 放到一个列表输出
from 包.notebook1 import add

list = []
for i in range(1000,2501):
    if(i%7 == 0 & i%5 == 0):
        list.append(i)
print(list)
# 2. 打印出0-20之间的数字，如果此数字能被3整除，输出英文”three”, 如果能被5整除,输出”five”，如果既能被3整除也
# 能被5整除，输出”threes+fives”, 要求用到continue.
# 1 Threes 27
# Threes ...
# 4 14
# fives Thees+fives
for i in range(0,21):
    if(i%3 == 0):
        print(i,"能被3整除")
        continue
    elif(i%5 == 0):
        print(i,"能被5整除")
        continue
    elif(i%3 == 0 & i%5 == 0):
        print(i,"既能被3也能被5整除")
        continue
# 3. 实现一个函数，要求对一个列表里面所有数字求和，如果里面含有非数字的元素。直接跳过。比如[1,2,3] 输出是5， 如果 是[1,2,4,”a”] 输出是7。 并在另外一个包(目录)里面调用这个函数
list1 = [1,2,3,'a',4]
add(list1)
# 4. 已有字典dic={“name”:”xiaozhang”,”sex”:”male”}, 访问字典 dic[“grade”]， 通过try... exception 把异常信息打印出来
dic={"name":"xiaozhang","sex":"male"}
try:
    print(dic["grade"])
except KeyError:
    print("主键不存在")
else:
    print(dict["grade"])
# 5. 实现一个不定长参数的函数def flexible(aa, *args, **kwargs):， 把传入的参数和值打印出来。比如传入参数是
# flexible(aa, 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
# 输出结果:(2, 3, 1, 2, 3)，{'a': 1, 'y': 5, 'b': 2, 'x': 4}
def flexible(aa,*args,**kwargs):
    list1 = []
    for i in args:
        list1.append(i)
    tuple1 = tuple(list1)
    print(tuple1)

    dict1 = {}
    for agr,value in kwargs.items():
        dict2 = {agr:value}
        dict1.update(dict2)

    print(dict1)

flexible("aa", 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b':2})