# 类型转换
list1 = ["a","1","c"]
print(type(list1))
var = tuple(list1)
print(type(var))

a = (("name","zhagnsan"),("sex","male"))
b = dict(a)
print(type(b))

#保留小数点
c=round(8.4567,2)
print(c)
print(int(c))

#字符串分割
path = '/Users/lixiangyu/IdeaProjects/apache-maven-3.6.0/bin: \
/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/bin: \
/Users/lixiangyu/Library/Android/sdk/build-tools/28.0.3: \
/Users/lixiangyu/Library/Android/sdk/platform-tools: \
/Users/lixiangyu/Library/Android/sdk/tools/bin: \
/Users/lixiangyu/Library/Android/sdk/tools: \
/Users/lixiangyu/anaconda3/bin: \
/Library/Frameworks/Python.framework/Versions/3.6/bin: \
/Library/Frameworks/Python.framework/Versions/3.6/bin: \
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:'

for item in path.split(":"):
    print(item)

path1 = '-rw-r--r--   1 root root   182 Nov  6 23:31 month.py'
list1 = path1.split()
print(list1[-4:])
print(path1.split(" "))

#字符串操作
a = "i love java"
print(a.replace("java","python"))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.startswith("i"))
print(a.endswith("v"))
print(a.index("love"))

list1=["i","love","python"]
print(" ".join(list1))

