# 1. 利用pip,安装第三方模块requests,描述你用什么方法来确认 安装是成功的。
import requests;

# 2. 把2.918转化为整形
print(int(2.918))

# 3. 把10进制数18转化为2进制数
print(bin(int("18",10)))

# 4. 用java 替换字符串:”Python is popular” 里面的Python，并把java 变换成JAVA
str = "Python is popular"
str1 = str.replace("Python","java")[0:4].upper()
str2 = str[7:]
print(str1+" "+str2)

# 5. 把列表 [1, 2, 3,4 5,6,7,8]里面的2, 4, 6,8 打印出来
list = [1,2,3,4,5,6,7,8]
print(list[1::2])

# 6. 创建一个字典，字典的key分别是name, sex, province , 修改原始province 的值 为新值”江苏”
dict = {"name":"tom","sex":"male","province":"jangsu"}
dict["province"] = "江苏"
print(dict)

# 7. Test_str=“Python was created in 1989, Python is using in AI, big data, IOT.” 按下列要求对上面文字做出处理。
# • 把上面文字中的所有大写转化为小写
# • 把这段话每个单词放到列表里面，不能不包含空格。
# • 把列表最中间的一个单词打印出来。
Test_str="Python was created in 1989, Python is using in AI, big data, IOT."
print(Test_str.lower())

list3 = Test_str.split()
print(list3)

center = (len(list3))/2
print(list3[int(center)])

# 8. list1=[“python”, 5,6, 8], list2=[“python”,”5”, 6, 8,10], 对list1和
# list2做出如下处理:
# • 把上面2个list的内容合并成一个
# • 利用set里面的方法，对合并后的list，去除重复元素。最后输出是还是list =[“python”, 5,6, 8,”5”,10] (顺序可以不一样)
list1=["python", 5,6, 8]
list2=["python","5", 6, 8,10]
list4 = list1+list2

set = set(list4)
print (set)



